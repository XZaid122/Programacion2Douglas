

package com.mycompany.vector;

import java.util.ArrayList;
import java.util.Collections;



public class Vector {

    public static void main(String[] args) {
        ArrayList<Integer> lista = new ArrayList();
         System.out.println(lista);
    System.out.println("El tamaño de la lista es: " +lista.size());
    System.out.println(lista);
    
    
    ArrayList<String> animales = new ArrayList();
        animales.add("gato");
        animales.add("perro");
        animales.add("conejo");
        animales.add("tortuga");
        animales.add("loro");
        System.out.println(animales);    
     String primerElemento = animales.get(0);
        System.out.println("Primer elemento: " + primerElemento);
        
        String centralElemento = animales.get(2);
        System.out.println("Elemento central: " + centralElemento);
        
        String ultimoElemento = animales.get(4);
        System.out.println("Ultimo elemento: " + ultimoElemento);
        
        ArrayList<String> datosPersonales = new ArrayList<>();

        datosPersonales.add("Douglas");
        datosPersonales.add("21"); 
        datosPersonales.add("163 cm"); 
        datosPersonales.add("Soltero"); 
        datosPersonales.add("Crespito Cra 14 69a06"); 
        datosPersonales.add("Cartagena");
        System.out.println(datosPersonales);
        
        
        ArrayList<String> it_companies = new ArrayList<>();
        it_companies.add("Facebook");
        it_companies.add("Google");
        it_companies.add("Microsoft");
        it_companies.add("Apple");
        it_companies.add("IBM");
        it_companies.add("Oracle");
        it_companies.add("Amazon");
        
        System.out.println("Lista de empresas de tecnologia:");
        System.out.println(it_companies);
        it_companies.add("Youtube");
        System.out.println(it_companies);

        System.out.println("Lista de empresas de tecnologia:");
        System.out.println(it_companies);
        System.out.println("La empresa Amazon esta en la lista? " + it_companies .contains("Amazon")); 
        Collections.sort(it_companies);
        System.out.println("Ordenando la lista:  " +it_companies);
        Collections.reverse(it_companies);
        System.out.println("Lista de empresas de tecnologia en orden descendente:");
        System.out.println(it_companies);
        it_companies.remove(1);
        System.out.println("Imprimiendo Lista despues de eliminacion" +it_companies);
        it_companies.clear();
System.out.println("Imprimiendo Lista despues de vaciada" +it_companies);

    }
}
