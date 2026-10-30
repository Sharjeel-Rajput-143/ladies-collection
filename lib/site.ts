export const SITE = {
  // Default website name. The owner can change it from the admin panel (Website), which then takes over.
  brand: "Ladies Collection",
  tagline: "Just on Bin Siddique Collection",
  // International format, digits only: 0331 6967181 -> 923316967181
  whatsappNumber: "923316967181",
  phoneDisplay: "0331 6967181",
  // Optional. When set, product links are added to the WhatsApp message.
  url: process.env.NEXT_PUBLIC_SITE_URL ?? "",
} as const;
