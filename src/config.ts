export const site = {
  name: "TailorLM",
  tagline: "Custom models, fitted to your business.",
  email: "contact@mcocdaa.com",
  url: "https://tailorlm.mcocdaa.com",
  github: "https://github.com/tailorlm",
  icp: import.meta.env.PUBLIC_ICP_BEIAN ?? "",
} as const;

export function mailto(subject = "TailorLM free problem review", body = ""): string {
  const parts = [`subject=${encodeURIComponent(subject)}`];
  if (body) {
    parts.push(`body=${encodeURIComponent(body.replace(/\r?\n/g, "\r\n"))}`);
  }
  return `mailto:${site.email}?${parts.join("&")}`;
}
