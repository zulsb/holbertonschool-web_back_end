import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return uploadPhoto()
    .then((response) => {
      createUser()
        .then((res) => {
          console.log(response.body, res.firstName, res.lastName);
        })
        .catch(() => {
          console.error('Signup system offline');
        });
    })
    .catch(() => {
      console.error('Signup system offline');
    });
}
