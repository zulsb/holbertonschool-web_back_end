export default function appendToEachArrayValue(array, appendString) {
  const aux = array;
  for (const i of array) {
    const value = array.indexOf(i);
    aux[value] = `${appendString}${i}`;
  }

  return aux;
}
