import { api } from 'boot/axios';
import { Project } from '@types';

export function useProject() {
  const fetchProjects = (): Promise<Project[]> => {
    return new Promise((resolve, reject) => {
      api
        .get<Project[]>('project/list/')
        .then((response) => {
          resolve(response.data);
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  };

  return {
    fetchProjects
  };
}
