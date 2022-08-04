package com.tema8;

public class Main {
    public static void main(String[] args) {
        Person person = new Person();
        person.setAge(30);
        person.setName("Marcos");
        person.setPhoneNumber(11569409);
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
        System.out.println("Phone Number: " + person.getPhoneNumber());

    }
}

class Person {
    private int age;
    private String name;
    private int phoneNumber;

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

}