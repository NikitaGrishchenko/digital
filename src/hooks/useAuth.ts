import { api } from 'boot/axios';
// import { useStore } from 'src/store'
// // import { IUserInfo } from 'src/types/auth'
// import { useRouter } from 'vue-router'

export function useAuth() {
  // const router = useRouter()
  // const store = useStore()


  const userLogin = (username: string, password: string) => {
    return new Promise((resolve, reject) => {
      api
        .post('auth/token/login/', {username , password})
        .then((response) => {
          resolve(response.data);
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  };

  // const userLogout = () => {
  //   return fetch(
  //     {
  //       method: 'POST',
  //       url: 'auth/token/logout/'
  //     },
  //     () => {
  //       store.commit('auth/logoutUser')
  //       void router.push({
  //         name: 'LoginPage'
  //       })
  //     }
  //   )
  // }

  // const getUserInfo = () => {
  //   return fetch<IUserInfo>({
  //     method: 'GET',
  //     url: 'auth/user-info/'
  //   })
  // }

  // const updateUserInfo = (userInfo: IUserInfo) => {
  //   return fetch<IUserInfo>({
  //     method: 'PATCH',
  //     url: 'auth/user-info/',
  //     data: userInfo
  //   })
  // }

  return {
    userLogin,
    // userLogout,
    // getUserInfo,
    // updateUserInfo,
  }
}
