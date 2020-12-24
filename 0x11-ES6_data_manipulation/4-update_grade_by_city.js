export default function updateStudentGradeByCity(listS, city, newGrades) {
  return listS.filter(
    (student) => student.location === city
  )
}
