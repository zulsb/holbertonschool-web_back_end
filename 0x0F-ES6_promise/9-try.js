export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (errors) {
    queue.push(`${errors.name}: ${errors.message}`);
  }
  queue.push('Guardrail was processed');
  return queue;
}
