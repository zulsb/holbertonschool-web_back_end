export default function getStudentIdsSum(listS) {
  return listS.reduce((total, student) => total + student.id, 0);
}
