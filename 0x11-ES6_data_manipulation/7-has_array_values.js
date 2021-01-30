export default function hasValuesFromArray(set, array) {
  return new Set([...new Set(array)].filter((x) => set.has(x))).size === array.length;
}
