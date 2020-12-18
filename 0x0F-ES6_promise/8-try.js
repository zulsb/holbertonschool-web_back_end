export default function divideFunction(numerator, denominator) {
  if (denominator !== 0) {
    return numerator / denominator;
  } else { 
  throw Error('cannot divide by 0');}
}
