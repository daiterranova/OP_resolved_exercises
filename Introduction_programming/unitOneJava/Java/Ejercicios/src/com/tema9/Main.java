package com.tema9;

public class Main {
    public static void main(String[] args){
    Cliente cliente = new Cliente();
    cliente.age = 23;
    cliente.name = "Francisco";
    cliente.telephone = 1604830;
    cliente.credit = 20000;
    System.out.println("El cliente " + cliente.name + " de " + cliente.age + " con el numero de telefono: " + cliente.telephone + " posee un credito de " + cliente.credit);
    Trabajador trabajador = new Trabajador();
    trabajador.age = 22;
    trabajador.name = "Martin";
    trabajador.telephone = 4560600;
    trabajador.salary = 40000;
        System.out.println("El trabajador " + trabajador.name + " de " + trabajador.age + " con el numero de telefono: " + trabajador.telephone + " tiene un salario mensual de " + trabajador.salary);
    }
}

class Persona {
    String name;
    int age;
    int telephone;
}

class Cliente extends Persona {
    int credit;
}

class Trabajador extends Persona{
    int salary;
}
