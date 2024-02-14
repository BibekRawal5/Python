import pandas as pd
    
def quarters(file, columns):
    quarters_dict = dict()
    
    for col in columns:
        quarters_dict[col] = [file[col].quantile(.75), file[col].quantile(.50), file[col].quantile(.25), 0]
    
    return quarters_dict

def take_inputs(file, columns):
    inputs = dict()
    for col in columns:
        inputs[col] = int(input(f"Enter {col}: ")) / file[col].max()
    return inputs

def calculate_numbers_pos_neg(file, columns, output_col, quarters_dict):
    number_pos_neg = dict()
    for col in columns:
        tmp_file =  file.drop([x for x in columns if x != col], axis=1)
        for i, quarter in enumerate(quarters_dict[col]):
            tmp = tmp_file[(tmp_file[col] > quarter)]
            tmppos = tmp[(tmp[output_col] == 1.000)]
            tmpneg = tmp[(tmp[output_col] == 0.000)]
            number_pos_neg[col + str(i)] = [tmppos.shape[0], tmpneg.shape[0]]
            tmp_file = tmp_file[tmp_file[col] <= quarter]  
    return number_pos_neg

def calculate_indexes(inputs, columns, quarters_dict):
    indexes = dict()
    for col in columns:
        for i, quarter in enumerate(quarters_dict[col]):
            if inputs[col] > quarter:
                indexes[col] = i
                break
    return indexes

 
def main():
    # filename = input("Enter the filename: ")
    filename = 'tmp.csv'
    file =  pd.read_csv(filename)
    file_copy = file.copy()
    total_pos = file[file['diabetes'] == 1].shape[0]
    total_neg = file[file['diabetes'] == 0].shape[0]
    columns = file.columns
    output_col = columns[-1]
    columns = columns.delete(-1)
    
    #normalizing the dataset
    for col in columns:
        file[col] = file[col] / file[col].max()
    
    #dictionary of each column quarters bootom least value      
    quarters_dict = quarters(file, columns)
    
    #dict to store number of positive and negative results of each columns
    numbers_pos_neg = calculate_numbers_pos_neg(file, columns, output_col, quarters_dict)
     
     

    #taking inputs for prediction
    inputs = take_inputs(file_copy, columns)
   
    #calculating indexes
    indexes = calculate_indexes(inputs, columns, quarters_dict)
    

    #calculating probabilities
    pos_prob = total_pos/(total_pos + total_neg)
    neg_prob = total_neg/(total_pos + total_neg)
    
    for col in columns:
        pos_prob *= numbers_pos_neg[col + str(indexes[col])][0] / total_pos
        neg_prob *= numbers_pos_neg[col + str(indexes[col])][1] / total_neg

    print(f"Positive probability = {pos_prob}, Negative probability = {neg_prob}")
    
    #Printing the result
    if(pos_prob > neg_prob):
        print(f"{output_col.capitalize()} POSIITVE")
    else:
        print(f"{output_col.capitalize()} NEGATIVE")

    
    
if __name__ == '__main__':
    main()