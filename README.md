# Dragon Remodelação

Site estático **Astro 7 + Tailwind CSS 4** em pt-PT, para pintura e remodelações em Lisboa.

## Desenvolvimento

Node 22.12+ (produção Node 24). `npm ci`, `npm run dev`. Para produção: `npm run build` gera `dist/`. `npm test` verifica JavaScript, lógica isolada e HTML compilado (executar após o build).

- `src/pages/index.astro`: página e metadata.
- `src/styles/global.css`: Tailwind via plugin Vite e CSS responsivo da identidade existente.
- `src/scripts/project.js`: navegação acessível e resumo de projeto local.
- `public/assets/`: quatro WebP locais; fontes/licenças em `ASSETS.md`.
- `vercel.json`: preset Astro, `npm ci`, build estático e saída `dist`.

## Conteúdo e privacidade

As fotografias e o vídeo externo são **ilustrativos**, não um portefólio de obras da empresa. Não há fotografia de equipa, testemunhos, contactos, certificações ou métricas inventados.

O formulário **não envia pedidos**: gera um resumo copiável, mantém os campos e não guarda dados em servidor ou localStorage. Contactos oficiais e backend aguardam confirmação. Os antigos módulos Gemini sem chave foram removidos; nenhuma chave/API é exposta no browser. Google Fonts e Phosphor são recursos externos; pedidos de navegação a esses fornecedores não contêm os dados do formulário.

## QA

`npm run build` e `npm test`: relatório de execução entregue com a alteração. A suite `qa/test.py` permite Playwright a 360/390/768/1440px com `BASE_URL=https://dragon-remodelacao.vercel.app` (ou servidor local em :8765). Valida imagens, overflow, menu/teclado, formulário repetido, área de transferência/fallback e reduced motion; guarda capturas locais em `qa/`.

**Limite conhecido:** QA browser local e screenshots não executados neste ambiente: sockets bloqueados e browser cloud não aceita file://. Testes lógicos usam DOM simulado, não substituem revisão visual real. Deve completar-se QA pós-deploy no browser autorizado.

## Histórico da revisão

Migração do HTML estático do commit `29f42b844bf285ae4f65fc0be4b965ffa3b57171`, preservando o mesmo repositório e projeto Vercel. O design mantém azul-marinho/branco, Inter e Phosphor; corrige falsas atribuições das imagens, foto 404 e falso sucesso do formulário original.

Publicação autorizada pelo proprietário em 25/10/2026. Domínios e permissões de acesso não alterados.

## Paleta Portugal (25/10/2026)

Verde `#00623b` nas zonas de marca, vermelho `#b5222a` nos botões/destaques (hover `#961c23`), base clara `#f7f6f0` e texto `#173c2b`. Azuis antigos substituídos também em cores secundárias, sombras, foco e theme-color. Layout, fotografias, conteúdos e funcionalidades mantidos. `python qa/contrast-check.py` verifica pares sólidos de texto, botões, foco e contornos de campos (WCAG AA); texto sobre fotografia requer verificação visual separada.
