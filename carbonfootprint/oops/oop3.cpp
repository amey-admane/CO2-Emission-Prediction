#include <iostream>
using namespace std;
class Rectangle;
class Triangle;

class Shape
{  
   public:
    
    double Dimension_1;
    double Dimension_2;
    
    void get_data()
    {
        cout<<"Enter dimension 1 : ";
        cin>>Dimension_1;
        cout<<"Enter dimension 2 : ";
        cin>>Dimension_2;
    }
    virtual void display_area(){
       cout<<"-----" ;
    }
};
class Rectangle : public Shape
{
    public:
    
    void display_area()
    {
        double Area_Rectangle = Dimension_1 * Dimension_2;
        cout<<"Area of rectangle : "<<Area_Rectangle<<endl;
    }
};

class Triangle : public Shape
{
    public:
    
    void display_area()
    {
        double Area_Triangle = 0.5 * Dimension_1 * Dimension_2;
        cout<<"Area of Triangle : "<<Area_Triangle<<endl;
    }
};

class Circle : public Shape
{
    public:
    double Dimension_2 = 0;
    
};

int main ()
{
    Rectangle r;
    Triangle t;
    Circle c;
    cout<<"Enter details for Rectangle : "<<endl;
    r.get_data();
    r.display_area();
    cout<<" \n\n";
    
    cout<<"Enter details for Triangle : "<<endl;
    t.get_data();
    t.display_area();
    cout<<" \n\n";
    
    cout<<"Enter details for Circle : "<<endl;
    c.get_data();
    c.display_area();
}


