export type Lang = "zh" | "en";

export const languages = {
  zh: {
    label: "中文",
    htmlLang: "zh-CN",
    ogLocale: "zh_CN",
  },
  en: {
    label: "English",
    htmlLang: "en",
    ogLocale: "en_US",
  },
} as const;

function normalize(path: string): string {
  const clean = path.startsWith("/") ? path : `/${path}`;
  return clean.replace(/\/+$/, "") || "/";
}

/** Build a path in the requested language. Chinese lives at the root, English under /en. */
export function localePath(lang: Lang, path: string): string {
  const clean = normalize(path);
  if (lang === "zh") return clean === "/" ? "/" : `${clean}/`;
  return clean === "/" ? "/en/" : `/en${clean}/`;
}

/** Given the current language and pathname, return the same page in the other language. */
export function alternatePath(lang: Lang, pathname: string): string {
  if (lang === "en") {
    return localePath("zh", pathname.replace(/^\/en(?=\/|$)/, "") || "/");
  }
  return localePath("en", pathname);
}
