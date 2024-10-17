const textoJSON = '{"nombre": "Carlos", "edad": 30, "salario": 3000}';

const objeto = JSON.parse(textoJSON, (clave, valor) => {
  return typeof valor === 'number' ? valor * 2 : valor;
});

console.log(objeto.nombre)
console.log(objeto.edad);  
console.log(objeto.salario);