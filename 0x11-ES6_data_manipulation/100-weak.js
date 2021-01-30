export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const counts = weakMap.get(endpoint);
  if (counts + 1 === 5) throw Error('Endpoint load is high');
  if (counts) {
    weakMap.set(endpoint, counts + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
}
