#include <cstdlib>

class Person {
public:
    Person(int);
    int get();
    void set(int);
    int fib();
private:
    int age;
    int fibHelp(int);
};

Person::Person(int n) {
    age = n;
}

int Person::get() {
    return age;
}

int Person::fibHelp(int n) {
    if (n <= 1) {
        return n;
    }
    return fibHelp(n - 1) + fibHelp(n - 2);
}

void Person::set(int n) {
    age = n;
}

int Person::fib() {
    return fibHelp(age);
}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_fib(Person* person){return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}

