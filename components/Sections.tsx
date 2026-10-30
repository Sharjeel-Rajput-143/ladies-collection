import Image from "next/image";
import { photo, type Category } from "@/lib/products";
import { SITE } from "@/lib/site";
import CategoryLink from "./CategoryLink";
import { FeatureIcon, LogoMark, WhatsAppIcon, type FeatureIconName } from "./Icons";
import Reveal from "./Reveal";
import WhatsAppLink from "./WhatsAppLink";

const FEATURES: { icon: FeatureIconName; title: string; text: string }[] = [
  { icon: "leaf", title: "Premium fabric", text: "Soft, breathable, true-to-colour" },
  { icon: "ruler", title: "Made to your size", text: "Custom dimensions & finishes" },
  { icon: "chat", title: "Free consultation", text: "Design advice on WhatsApp" },
  { icon: "truck", title: "Delivery & fitting", text: "Safe delivery to your door" },
];

const STEPS = [
  {
    title: "Pick a design",
    text: "Browse lawn, kurtis, abayas and dresses. Switch tabs to see more styles.",
  },
  {
    title: "Tap Get Price",
    text: "WhatsApp opens with the product name and details already filled in.",
  },
  {
    title: "Get your quote",
    text: "We reply with the price, size options and delivery time.",
  },
];

const LIFESTYLE_POINTS = [
  "Pick your fabric, print and size",
  "Skilled carpenters, checked at every step",
  "Delivery and fitting at your home",
];

export function TrustStrip() {
  return (
    <section className="strip" aria-label="Why choose us">
      <div className="container strip-grid">
        {FEATURES.map((feature) => (
          <div className="strip-item" key={feature.title}>
            <span className="strip-icon">
              <FeatureIcon name={feature.icon} />
            </span>
            <div>
              <h3>{feature.title}</h3>
              <p>{feature.text}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export function Lifestyle() {
  return (
    <section className="section section-soft">
      <div className="container lifestyle">
        <Reveal className="lifestyle-media">
          <div className="lifestyle-main">
            <Image
              src={photo("photo-1600607687939-ce8a6c25118c")}
              alt="Rack of folded women\u2019s clothing in a boutique"
              fill
              sizes="(min-width: 900px) 560px, 100vw"
              className="media-img"
            />
          </div>
          <div className="lifestyle-inset">
            <Image
              src={photo("photo-1687422810663-c316494f725a")}
              alt="Tailor stitching fabric in the workshop"
              fill
              sizes="(min-width: 900px) 260px, 50vw"
              className="media-img"
            />
          </div>
        </Reveal>
        <Reveal className="lifestyle-copy" delay={100}>
          <p className="eyebrow">Crafted around your space</p>
          <h2>Styles picked for every season, not just one trend</h2>
          <p>
            Every piece is quality-checked before it reaches you. Share your size and preference and
            we&rsquo;ll help you find the right fit.
          </p>
          <ul className="checklist">
            {LIFESTYLE_POINTS.map((point) => (
              <li key={point}>{point}</li>
            ))}
          </ul>
          <WhatsAppLink className="btn btn-wa btn-lg">
            <WhatsAppIcon className="btn-icon" />
            Talk to our team
          </WhatsAppLink>
        </Reveal>
      </div>
    </section>
  );
}

export function HowItWorks() {
  return (
    <section className="section" id="how">
      <div className="container">
        <Reveal className="section-head">
          <p className="eyebrow">Simple process</p>
          <h2>How it works</h2>
        </Reveal>
        <ol className="steps">
          {STEPS.map((step, i) => (
            <li key={step.title}>
              <Reveal className="step" delay={i * 100}>
                <span className="step-num">{i + 1}</span>
                <h3>{step.title}</h3>
                <p>{step.text}</p>
              </Reveal>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}

export function CtaBand() {
  return (
    <section className="cta-band" id="contact">
      <Image
        src={photo("photo-1683115099191-51e617fc5ff1")}
        alt=""
        fill
        sizes="100vw"
        className="media-img"
      />
      <div className="cta-shade" />
      <div className="container cta-content">
        <Reveal className="cta-inner">
          <h2>Can&rsquo;t find your perfect design?</h2>
          <p>Send us a photo or your idea on WhatsApp and our team will build it for you.</p>
          <WhatsAppLink className="btn btn-wa btn-lg">
            <WhatsAppIcon className="btn-icon" />
            Chat with us on WhatsApp
          </WhatsAppLink>
          <p className="cta-phone">
            Or call / message: <a href={`tel:+${SITE.whatsappNumber}`}>{SITE.phoneDisplay}</a>
          </p>
        </Reveal>
      </div>
    </section>
  );
}

export function Footer({ brand, categories }: { brand: string; categories: Category[] }) {
  return (
    <footer className="footer">
      <div className="container footer-grid">
        <div className="footer-brand">
          <a href="#top" className="logo">
            <LogoMark className="logo-mark" />
            <span>{brand}</span>
          </a>
          <p>{SITE.tagline}. Lawn, kurtis, abayas and party dresses.</p>
        </div>

        <div>
          <h4>Shop</h4>
          <ul>
            {categories.map((c) => (
              <li key={c.id}>
                <CategoryLink id={c.id} className="footer-link">
                  {c.label}
                </CategoryLink>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h4>Help</h4>
          <ul>
            <li>
              <a href="#how">How it works</a>
            </li>
            <li>
              <a href="#contact">Contact us</a>
            </li>
          </ul>
        </div>

        <div>
          <h4>Contact</h4>
          <ul>
            <li>
              <a href={`tel:+${SITE.whatsappNumber}`}>{SITE.phoneDisplay}</a>
            </li>
            <li>
              <WhatsAppLink className="footer-link">Chat on WhatsApp</WhatsAppLink>
            </li>
          </ul>
        </div>
      </div>
      <div className="container footer-bottom">
        © {new Date().getFullYear()} {brand}. All rights reserved.
      </div>
    </footer>
  );
}

export function WhatsAppFab() {
  return (
    <WhatsAppLink className="fab">
      <WhatsAppIcon className="fab-icon" />
      <span className="sr-only">Chat on WhatsApp</span>
    </WhatsAppLink>
  );
}
