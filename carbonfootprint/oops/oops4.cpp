#include <iostream>
using namespace std;

int spoilt = 0;
class Election
{
public:
    int count = 0;
    virtual void display_votes() = 0;
};

class a : public Election
{
public:
    void display_votes()
    {
        cout << "Total votes recieved by Candidate_1 : " << count << endl;
    }
};

class b : public Election
{
public:
    void display_votes()
    {
        cout << "Total votes recieved by Candidate_2 : " << count << endl;
    }
};

class c : public Election
{
public:
    void display_votes()
    {
        cout << "Total votes recieved by Candidate_3 : " << count << endl;
    }
};

class d : public Election
{
public:
    void display_votes()
    {
        cout << "Total votes recieved by Candidate_4 : " << count << endl;
    }
};

class e : public Election
{
public:
    void display_votes()
    {
        cout << "Total votes recieved by Candidate_5 : " << count << endl;
    }
};

int main()
{
    a Candidate_1;
    b Candidate_2;
    c Candidate_3;
    d Candidate_4;
    e Candidate_5;

    int voters;
    cout << "Enter the number of voters : ";
    cin >> voters;
    int choice;
    cout << "Enter the candidate you want to vote from (1 to 5) : " << endl;
    for (int i = 1; i <= voters; i++)
    {
        cout << "Member " << i << "Whom would you vote for : ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            Candidate_1.count++;
            break;
        case 2:
            Candidate_2.count++;
            break;
        case 3:
            Candidate_3.count++;
            break;
        case 4:
            Candidate_4.count++;
            break;
        case 5:
            Candidate_5.count++;
            break;
        default:
            spoilt++;
            break;
        }
    }
    cout << endl
         << "Final Election Result : " << endl;
    Candidate_1.display_votes();
    Candidate_2.display_votes();
    Candidate_3.display_votes();
    Candidate_4.display_votes();
    Candidate_5.display_votes();
    cout << "Non-countable votes / Spoilt votes : " << spoilt;
}
