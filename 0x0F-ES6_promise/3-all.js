import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return uploadPhoto().then((r) => {
    createUser().then((val) => {
      console.log(r.body, val.firstName, val.lastName);
    }).catch(() => {
      console.error('Signup system offline');
    });
  }).catch(() => {
    console.error('Signup system offline');
  });
}
