#include <iostream>
#include <conio.h>
#include <fstream>
#include <stdlib.h>

using namespace std;

class Node{
	public:
		Node *parent;
		int m , n;
	
	Node(){
	}
	
	Node(int m, int n, Node *parent)
	{
		this->m = m;
		this->n = n;
		this->parent = parent;
	}
};

class Stack{
	public:
		Node *array[100];
		static int top;
		
		void push(Node *p)
		{
			array[++top] = p;
		}
		
		Node *pop()
		{
			return array[top--];
		}
};

int Stack::top = -1;

int main()
{
	int i = 0, height = 0, width = 0, j = 0, k = 0, l = 0, r, c;
	int si, sj, ei, ej;
	char ch;	
	char maze[100][100];
	
	ifstream my_file("maze1.txt");
	
	while(!my_file.eof())
	{
		my_file.get(ch);
		if(ch == '\n')
		{
			i++;
			if(j > width)
			{
				width = j;
			}
			j = 0;
			continue;
		}
		maze[i][j++] = ch;
	}
	
	height = ++i;

	for(k = 0; k < height; k++)
	{
		for(l = 0; l < width; l++)
		{
			if(maze[k][l] == 'A')
			{
				si = k;
				sj = l;
			}
			else if(maze[k][l] == 'B')
			{
				ei = k;
				ej = l;
			}
			cout<< maze[k][l];
		}
		cout<<"\n";
	}
	Node *node = (Node *)malloc(sizeof(Node));
	node->m = si;
	node->n = sj;
	node->parent = NULL;
	Stack frontier;
	frontier.push(node);
	char explored[100][100];
	int cells[height * width], ci = 0;
	
	while(1)
	{
		Node *node = (Node *)malloc(sizeof(Node));
		node = frontier.pop();
		r = node->m;
		c = node->n;

		if(r == ei && c == ej)
		{
			while(node->parent != NULL)
			{
				r = node->m;
				c = node->n;
				cells[ci++] = r * 10 + c;
				node = node->parent; 
			}
			break;
		}
		
		explored[node->m][node->n] = 'y';

		Node *child = (Node *)malloc(sizeof(Node));
		//left neighbour
		if(c - 1 >= 0 && explored[r][c-1] != 'y' && maze[r][c-1] != '#')
		{
			child->m = r;
			child->n = c-1;
			child->parent = node;
			frontier.push(child);
		}
		//right neighbour
		if(c + 1 < width && explored[r][c+1] != 'y' && maze[r][c+1] != '#')
		{
			child->m = r;
			child->n = c+1;
			child->parent = node;
			frontier.push(child);
		}
		//Top neighbour
		if(r - 1 >= 0 && explored[r-1][c] != 'y' && maze[r-1][c] != '#')
		{
			child->m = r - 1;
			child->n = c;
			child->parent = node;
			frontier.push(child);
		}
		//Bottom neighbour
		if(r+1 < height && explored[r+1][c] != 'y' && maze[r+1][c] != '#')
		{
			child->m = r + 1;
			child->n = c;
			child->parent = node;
			frontier.push(child);
		}

	}
	
	
	cout << "\n\nSOLVED : \n\n";
	//solving 
	for(k = 0; k < ci; k++)
	{
		int tp = cells[k];
		r = tp/10;
		c = tp % 10;
		if(maze[r][c] != 'B')
			maze[r][c] = '-';
	}
	
	for(k = 0; k < height; k++)
	{
		for(l = 0; l < width; l++)
		{
			cout<< maze[k][l];
		}
		cout<<"\n";
	}
	
	
}
