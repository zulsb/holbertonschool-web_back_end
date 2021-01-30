export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw Error('Position outside range');

  const buffer = new ArrayBuffer(length);
  const newArray = new DataView(buffer);
  newArray.setUint8(position, value);

  return newArray;
}
