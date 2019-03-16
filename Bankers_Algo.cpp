#include <iostream>
using namespace std;
int main()
{
	int n,a,done=0,flag=1;
	cout<<"Enter No. of processes: "<<endl;
	cin>>n;
	cout<<"Enter no of resources : "<<endl;
	cin>>a;
	int mat[n][a];
	int req[n][a];
	int avail[a];
	int finish[n];
	for(int i=0;i<n;i++)
	{
		cout<<"Enter the resources allocated to process P"<<i<<endl;
		for(int j=0;j<a;j++)
		{
			cin>>mat[i][j];
		}
		finish[i]=0;
	}
	for(int i=0;i<n;i++)
	{
		cout<<"Enter the request of resource by process P"<<i<<endl;
		for(int j=0;j<a;j++)
		{
			cin>>req[i][j];
		}
	}
	for(int i=0;i<a;i++)
	{
		avail[i]=0;
		
	}
	while(done!=n)
	{
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<a&&flag==1&&finish[i]==0;j++)
			{
				if(mat[i][j]+avail[j]<req[i][j])
				{
					flag=0;
				}
				
			}
			if(flag==1&&finish[i]==0)
			{
				for(int k=0;k<a;k++)
				{
					avail[k]=avail[k]+mat[i][k];
					
					//req[][]
				}
				cout<<"Allocated to Process P"<<i<<endl;
				done++;
				finish[i]=1;
			}
			else
			{
				flag=1;
			}
		}
	}
	
	
}
