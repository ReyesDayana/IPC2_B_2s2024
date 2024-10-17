const textoJSON = '{"nombre": "Ana", "apellido": "Martinez","edad": 25, "casado": false}';
const objeto = JSON.parse(textoJSON);

console.log(objeto.nombre); 
console.log(objeto.edad);   
console.log(objeto.casado);
console.log(objeto.apellido)