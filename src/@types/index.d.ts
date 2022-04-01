export interface Project {
  id: number;
  img: string | null;
  name: string;
  link: string;
  description: string | null;
  order: number | null;
}
export interface TeammateSocial {
  id: number;
  link: string;
  icon: string;
}
export interface Teammate {
  id: number;
  username: string;
  img: string | null;
  firstName: string;
  lastName: string;
  position: { name: string } | null;
  social: TeammateSocial;
  order: number | null;
  dontShowTheUser: boolean;
}
export type Tag = {
  id: number | null;
  name: string;
};
export interface Article {
  id: number;
  author: Teammate[];
  img: string | null;
  dateOfPublication: string;
  dontShowTheArticle: boolean | null;
  numberOfViews: number;
  preview: string;
  tag: Tag | null;
  text: string;
  name: string;
}

export interface Captcha {
  uuid: string;
  image: string;
}
