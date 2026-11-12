export const site = {
  name: "TailorLM",
  tagline: "量体裁模",
  email: "contact@mcocdaa.com",
  url: "https://tailorlm.mcocdaa.com",
  github: "https://github.com/tailorlm",
  icp: import.meta.env.PUBLIC_ICP_BEIAN ?? "",
} as const;

export function mailto(subject = "TailorLM 诊断咨询", body = ""): string {
  const params = new URLSearchParams({ subject });
  if (body) {
    params.set("body", body);
  }
  return `mailto:${site.email}?${params.toString()}`;
}
