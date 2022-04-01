import { api } from 'boot/axios';
import { Captcha } from '@types';
import { AxiosResponse } from 'axios';

export function useCaptcha() {
  const fetchCaptcha = (): Promise<AxiosResponse<Captcha>> => {
    return new Promise((resolve, reject) => {
      api
        .get<Captcha>('captcha/generate/')
        .then((response) => {
          resolve(response);
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  };

  const sendCaptcha = (
    uuid: string,
    answer: string
  ): Promise<AxiosResponse> => {
    return new Promise<AxiosResponse>((resolve, reject) => {
      api
        .post('captcha/encode/', {
          uuid: uuid,
          userAnswer: answer
        })
        .then((response) => {
          resolve(response);
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  };

  const updateCaptcha = async (
    uuid: string
  ): Promise<AxiosResponse<Captcha>> => {
    return new Promise((resolve, reject) => {
      api
        .get<Captcha>(`captcha/update/${uuid}`)
        .then((response) => {
          resolve(response);
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  };

  return {
    fetchCaptcha,
    sendCaptcha,
    updateCaptcha
  };
}
