import { api } from 'boot/axios';
import { Teammate } from '@types';

export function useTeam() {
  const fetchTeammates = (): Promise<Teammate[]> => {
    return new Promise((resolve, reject) => {
      api
        .get<Teammate[]>('/auth/list')
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
    fetchTeammates
  };
}
