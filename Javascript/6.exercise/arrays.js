/* Crea un archivo JS que contenga las siguientes líneas

- Una variable que contenga la lista de la compra (mínimo 5 elementos)

- Modifica la lista de la compra y añádele "Aceite de Girasol"

- Vuelve a modificar la lista de la compra eliminando "Aceite de Girasol"

- Una lista de tus 3 películas favoritas (objetos con propiedades: titulo, director, fecha)

- Una nueva lista que contenga las películas posteriores al 1 de enero de 2010 (utilizando filter)

- Una nueva lista que contenga los directores de la lista de películas original (utilizando map)

- Una nueva lista que contenga los títulos de la lista de películas original (utilizando map) 

- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando concat) 

- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando el factor de propagación) */

let shoppingList = ["water", "milk", "sugar", "tea", "ginger"];

shoppingList.push("Aceite de girasol");

shoppingList.pop("Aceite de girasol");

/* console.log(shoppingList); */

const favoriteMovies = [
  {
    title: "Matrix",
    director: "Watchoski Brothers",
    releaseDate: new Date(1999, 6, 10),
  },
  {
    title: "Hercules",
    director: "Ron Clementes",
    releaseDate: new Date(1997, 7, 3),
  },
  {
    title: "Split",
    director: "M. Night Shyamalan",
    releaseDate: new Date(2016, 9, 26),
  },
];
/* 
console.log(favoriteMovies); */

const filteredMovies = favoriteMovies.filter(
  (movie) => movie.releaseDate > new Date(2010, 1, 1)
);

/* console.log(filterMovies); */

const directors = favoriteMovies.map((movie) => movie.director);

/* console.log(directors); */

const titles = favoriteMovies.map((movie) => movie.title);

/* console.log(titles); */

const newList = directors.concat(titles);

const newList2 = [...directors, ...titles];

/* console.log(newList2); */
