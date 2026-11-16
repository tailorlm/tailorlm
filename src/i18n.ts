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

/** Build a path in the requested language. English lives at the root, Chinese under /zh. */
export function localePath(lang: Lang, path: string): string {
  const clean = normalize(path);
  if (lang === "en") return clean === "/" ? "/" : `${clean}/`;
  return clean === "/" ? "/zh/" : `/zh${clean}/`;
}

/** Given the current language and pathname, return the same page in the other language. */
export function alternatePath(lang: Lang, pathname: string): string {
  if (lang === "zh") {
    return localePath("en", pathname.replace(/^\/zh(?=\/|$)/, "") || "/");
  }
  return localePath("zh", pathname);
}
