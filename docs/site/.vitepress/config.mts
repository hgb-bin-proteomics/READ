import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: "/READ/",
  srcDir: "md",
  title: "READ",
  description: "TMTpro-18plex quantification for [single cell] DIA and DDA searches with Chimerys, Spectronaut, and DIA-NN.",
  head: [
    [
      "link",
      {
        rel: "icon",
        href: "https://github.com/hgb-bin-proteomics/READ/raw/master/docs/logo/logo.png",
      },
    ],
  ],
  markdown: {
   theme: {
     light: "catppuccin-latte",
     dark: "catppuccin-mocha",
    },
  },
  themeConfig: {
    logo: {
      src: "https://github.com/hgb-bin-proteomics/READ/raw/master/docs/logo/logo.png",
      alt: "logo",
    },
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "About", link: "/about" },
      { text: "Documentation", link: "/docs/docs_intro" },
      { text: "Contact", link: "/contact" },
    ],
    sidebar: [
      {
        items: [
          { text: "About", link: "/about" },
          { text: "Documentation", items:
            [
              { text: "Introduction", link: "/docs/docs_intro" },
              { text: "Installation", link: "/docs/docs_install" },
              { text: "Example", link: "/docs/docs_example" },
              { text: "Usage", link: "/docs/docs_usage" },
              { text: "Configuration", link: "/docs/docs_config" },
              { text: "Output", link: "/docs/docs_output" },
              { text: "Batch Processing", link: "/docs/docs_batch" },
            ]
          },
          { text: "Help", link: "/contact" },
        ],
      },
    ],
    footer: {
      message: "Released under the MIT License.",
      copyright: "Copyright © 2026 Micha J. Birklbauer"
    },
    socialLinks: [{ icon: "github", link: "https://github.com/hgb-bin-proteomics/READ" }],
    search: {
        provider: 'local'
    },
  },
})
