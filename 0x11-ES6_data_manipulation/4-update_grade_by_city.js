export default function updateStudentGradeByCity(listS, city, newGrades) {
  return listS.filter(
    (student) => student.location === city,
  ).map((student) => Object.assign(
    student,
    { grade: newGrades.filter((grade) => student.id === grade.studentId)[0] ? newGrades.filter((grade) => student.id === grade.studentId)[0].grade : 'N/A' },
  ));
}
