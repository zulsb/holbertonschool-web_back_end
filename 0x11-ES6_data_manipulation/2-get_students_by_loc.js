export default function getStudentsByLocation(ListStudents, city) {
  return ListStudents.filter((student) => student.location === city);
}
