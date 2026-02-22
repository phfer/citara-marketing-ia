# FIREVON - Logotipos em SVG
## Pronto para copiar, colar no Figma/Illustrator e exportar como PNG

---

# VARIAÇÃO 1 - FIREVON (Wordmark Minimal)

```svg
<svg width="400" height="100" viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <!-- Fundo transparente -->
  <rect width="400" height="100" fill="transparent"/>

  <!-- Texto Principal -->
  <text x="50%" y="50" font-family="Inter, SF Pro Display, sans-serif" font-weight="700" font-size="48" fill="#1A1F36" text-anchor="middle" letter-spacing="-1">FIREVON</text>

  <!-- Sublinhado Orange -->
  <line x1="70" y1="65" x2="330" y2="65" stroke="#FF6B35" stroke-width="4" stroke-linecap="round"/>

  <!-- Tagline -->
  <text x="50%" y="85" font-family="Inter, SF Pro Text, sans-serif" font-weight="400" font-size="12" fill="#718096" text-anchor="middle" letter-spacing="0.5">PREVISIBILIDADE EM EXECUÇÃO</text>
</svg>
```

---

# VARIAÇÃO 2 - FireVon (Camel Case Dinâmico)

```svg
<svg width="450" height="120" viewBox="0 0 450 120" xmlns="http://www.w3.org/2000/svg">
  <rect width="450" height="120" fill="transparent"/>

  <!-- Triângulo Esquerdo -->
  <polygon points="40,40 55,60 25,60" fill="#FF6B35" opacity="0.9"/>
  <polygon points="40,55 55,75 25,75" fill="#FF6B35" opacity="0.6"/>

  <!-- Texto Principal - F em Bold -->
  <text x="70" y="65" font-family="Inter, SF Pro Display, sans-serif" font-weight="700" font-size="52" fill="#1A1F36">F</text>

  <!-- Texto Principal - ireVon em Regular -->
  <text x="98" y="65" font-family="Inter, SF Pro Display, sans-serif" font-weight="400" font-size="52" fill="#1A1F36">ireVon</text>

  <!-- Triângulo Direito -->
  <polygon points="380,40 395,60 365,60" fill="#FF6B35" opacity="0.6"/>
  <polygon points="380,55 395,75 365,75" fill="#FF6B35" opacity="0.9"/>

  <!-- Tagline -->
  <text x="50%" y="95" font-family="Inter, SF Pro Text, sans-serif" font-weight="400" font-size="11" fill="#718096" text-anchor="middle" letter-spacing="0.5">crescimento previsível. sistema integrado.</text>
</svg>
```

---

# VARIAÇÃO 3 - Monograma FV

```svg
<svg width="300" height="150" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="300" height="150" fill="transparent"/>

  <!-- Monograma FV Hexagonal -->
  <g stroke="#00D4C7" stroke-width="3" fill="none">
    <!-- Letra F -->
    <path d="M 70,30 L 70,70 M 70,30 L 100,30 M 70,50 L 90,50"/>

    <!-- Letra V integrada -->
    <path d="M 70,70 L 100,90 L 70,90"/>
  </g>

  <!-- Círculo sutil ao redor -->
  <circle cx="85" cy="60" r="45" stroke="#1A1F36" stroke-width="1.5" fill="none" opacity="0.3"/>

  <!-- Wordmark abaixo -->
  <text x="50%" y="130" font-family="Inter, SF Pro Display, sans-serif" font-weight="400" font-size="18" fill="#1A1F36" text-anchor="middle" letter-spacing="2">FIREVON</text>
</svg>
```

---

# VARIAÇÃO 4 - firevon (Lowcase Acessível)

```svg
<svg width="400" height="100" viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="100" fill="transparent"/>

  <!-- Arcos sobre cada letra -->
  <g stroke="#FF6B35" stroke-width="2" fill="none">
    <path d="M 80,30 Q 85,22 90,30"/>
    <path d="M 110,30 Q 115,22 120,30"/>
    <path d="M 140,30 Q 145,22 150,30"/>
    <path d="M 170,30 Q 175,22 180,30"/>
    <path d="M 200,30 Q 205,22 210,30"/>
    <path d="M 230,30 Q 235,22 240,30"/>
    <path d="M 260,30 Q 265,22 270,30"/>
    <path d="M 290,30 Q 295,22 300,30"/>
  </g>

  <!-- Texto Lowcase -->
  <text x="50%" y="60" font-family="Inter, SF Pro Display, sans-serif" font-weight="500" font-size="40" fill="#2D3748" text-anchor="middle" letter-spacing="3">firevon</text>

  <!-- Tagline -->
  <text x="50%" y="85" font-family="Inter, SF Pro Text, sans-serif" font-weight="400" font-size="11" fill="#718096" text-anchor="middle">menos achismo. mais resultado.</text>
</svg>
```

---

# VARIAÇÃO 5 - FIRE · VON (Two Words)

```svg
<svg width="400" height="130" viewBox="0 0 400 130" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#FF6B35;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00D4C7;stop-opacity:1" />
    </linearGradient>
  </defs>

  <rect width="400" height="130" fill="transparent"/>

  <!-- Texto Principal -->
  <text x="50%" y="55" font-family="Inter, SF Pro Display, sans-serif" font-weight="700" font-size="52" fill="#1A1F36" text-anchor="middle">FIRE <tspan fill="#718096" font-size="40">·</tspan> VON</text>

  <!-- Seta Ascendente Gradiente -->
  <path d="M 140,70 L 260,70 L 260,70" stroke="url(#grad1)" stroke-width="3" fill="none" stroke-linecap="round"/>
  <polygon points="260,70 250,65 250,75" fill="#00D4C7"/>

  <!-- Tagline -->
  <text x="50%" y="105" font-family="Inter, SF Pro Text, sans-serif" font-weight="400" font-size="11" fill="#718096" text-anchor="middle">onde estratégia vira rotina e resultado</text>
</svg>
```

---

# VARIAÇÃO 6 - F/V Abstrato (Momentum)

```svg
<svg width="300" height="150" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="300" height="150" fill="transparent"/>

  <!-- Símbolo F/V Abstrato -->
  <g>
    <!-- F (Laranja) -->
    <path d="M 70,40 L 70,70 L 100,70 L 100,55 L 85,55 L 85,48 L 95,48 L 95,40 Z" fill="#FF6B35"/>

    <!-- V (Teal) -->
    <path d="M 110,40 L 130,70 L 150,40 Z" fill="#00D4C7"/>

    <!-- Linha de fundação -->
    <line x1="60" y1="85" x2="160" y2="85" stroke="#1A1F36" stroke-width="3"/>
  </g>

  <!-- Wordmark -->
  <text x="50%" y="125" font-family="Inter, SF Pro Display, sans-serif" font-weight="700" font-size="16" fill="#1A1F36" text-anchor="middle" letter-spacing="3">FIREVON</text>
</svg>
```

---

# COMO USAR ESTES SVGs

## Opção 1: Figma
1. Copie o código SVG
2. Crie um novo arquivo no Figma
3. Vá em: Plugins → SVG Code
4. Cole o código e clique "Place SVG"

## Opção 2: Illustrator
1. Crie um novo documento
2. Arquivo → Importar
3. Selecione "All Files" e escolha um arquivo .svg (salve o código como .txt primeiro)
4. Ou cole diretamente no Illustrator

## Opção 3: Navegador (rápido)
1. Salve o código como arquivo .svg
2. Abra diretamente no Chrome/Edge
3. Print Screen ou ferramenta de captura
4. Editar no Photoshop/Canva

## Opção 4: Conversor Online
1. Salve o código como .svg
2. Acesse: svgtopng.com
3. Upload do SVG → Download PNG

---

# VERSÃO TODAS JUNTAS (PARA COMPARAÇÃO)

```svg
<svg width="800" height="600" viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="600" fill="#F7FAFC"/>

  <!-- Título -->
  <text x="400" y="40" font-family="Inter, sans-serif" font-weight="700" font-size="24" fill="#1A1F36" text-anchor="middle">FIREVON - VARIAÇÕES DE LOGOTIPO</text>

  <!-- Variação 1 -->
  <text x="100" y="100" font-family="Inter, sans-serif" font-weight="600" font-size="14" fill="#718096">1. WORDMARK MINIMAL</text>
  <text x="400" y="150" font-family="Inter, sans-serif" font-weight="700" font-size="48" fill="#1A1F36" text-anchor="middle" letter-spacing="-1">FIREVON</text>
  <line x1="260" y1="165" x2="540" y2="165" stroke="#FF6B35" stroke-width="3"/>

  <!-- Variação 2 -->
  <text x="100" y="220" font-family="Inter, sans-serif" font-weight="600" font-size="14" fill="#718096">2. CAMEL CASE DINÂMICO</text>
  <polygon points="260,240 270,255 250,255" fill="#FF6B35"/>
  <text x="275" y="255" font-family="Inter, sans-serif" font-weight="700" font-size="48" fill="#1A1F36">F</text>
  <text x="300" y="255" font-family="Inter, sans-serif" font-weight="400" font-size="48" fill="#1A1F36">ireVon</text>
  <polygon points="520,240 530,255 510,255" fill="#FF6B35"/>

  <!-- Variação 3 -->
  <text x="100" y="310" font-family="Inter, sans-serif" font-weight="600" font-size="14" fill="#718096">3. MONOGRAMA FV</text>
  <circle cx="400" cy="350" r="40" stroke="#00D4C7" stroke-width="3" fill="none"/>
  <path d="M 380,330 L 380,370 M 380,330 L 400,330 M 380,350 L 395,350" stroke="#00D4C7" stroke-width="3"/>
  <path d="M 380,370 L 400,390 L 380,390" stroke="#00D4C7" stroke-width="3"/>
  <text x="400" y="420" font-family="Inter, sans-serif" font-weight="400" font-size="18" fill="#1A1F36" text-anchor="middle" letter-spacing="2">FIREVON</text>

  <!-- Variação 4 -->
  <text x="100" y="470" font-family="Inter, sans-serif" font-weight="600" font-size="14" fill="#718096">4. LOWCASE ACESSÍVEL</text>
  <text x="400" y="510" font-family="Inter, sans-serif" font-weight="500" font-size="40" fill="#2D3748" text-anchor="middle" letter-spacing="3">firevon</text>

  <!-- Variação 5 -->
  <text x="600" y="100" font-family="Inter, sans-serif" font-weight="600" font-size="14" fill="#718096">5. TWO WORDS</text>
  <text x="710" y="145" font-family="Inter, sans-serif" font-weight="700" font-size="40" fill="#1A1F36" text-anchor="middle">FIRE</text>
  <text x="665" y="145" font-family="Inter, sans-serif" font-size="30" fill="#718096">·</text>
  <text x="760" y="145" font-family="Inter, sans-serif" font-weight="700" font-size="40" fill="#1A1F36" text-anchor="middle">VON</text>
  <line x1="620" y1="160" x2="800" y2="160" stroke="url(#grad)" stroke-width="2"/>
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#FF6B35"/>
      <stop offset="100%" style="stop-color:#00D4C7"/>
    </linearGradient>
  </defs>

  <!-- Variação 6 -->
  <text x="600" y="220" font-family="Inter, sans-serif" font-weight="600" font-size="14" fill="#718096">6. ABSTRATO F/V</text>
  <rect x="690" y="250" width="15" height="40" fill="#FF6B35"/>
  <rect x="710" y="250" width="10" height="20" fill="#FF6B35"/>
  <rect x="710" y="275" width="15" height="15" fill="#FF6B35"/>
  <polygon points="740,250 760,290 780,250" fill="#00D4C7"/>
  <line x1="680" y1="300" x2="790" y2="300" stroke="#1A1F36" stroke-width="3"/>
  <text x="735" y="330" font-family="Inter, sans-serif" font-weight="700" font-size="16" fill="#1A1F36" text-anchor="middle" letter-spacing="2">FIREVON</text>

  <!-- Legenda cores -->
  <rect x="50" y="550" width="20" height="20" fill="#FF6B35"/>
  <text x="80" y="565" font-family="Inter, sans-serif" font-size="12" fill="#1A1F36">Fire Orange #FF6B35</text>

  <rect x="200" y="550" width="20" height="20" fill="#1A1F36"/>
  <text x="230" y="565" font-family="Inter, sans-serif" font-size="12" fill="#1A1F36">Deep Navy #1A1F36</text>

  <rect x="350" y="550" width="20" height="20" fill="#00D4C7"/>
  <text x="380" y="565" font-family="Inter, sans-serif" font-size="12" fill="#1A1F36">Electric Teal #00D4C7</text>
</svg>
```

---

# COMO EXPORTAR COMO PNG

## Método Rápido (Thauane pode fazer):

1. **Abra o Figma**
2. **Plugins** → Procure por "SVG Code"
3. **Cole o código** de uma variação
4. **Clique em "Place SVG"**
5. **Clique no SVG criado** → Frame do objeto
6. **Export** → Exportar como PNG (2x ou 3x)

## Método Alternativo:

1. Salve cada SVG como arquivo `.svg`
2. Arraste para o navegador (Chrome)
3. Botão direito → Salvar imagem como...
4. Abrir no Photoshop/Canva e exportar PNG em alta resolução

---

**Instruções para Thauane:**
- Copiar os códigos acima
- Colar no Figma via plugin "SVG Code"
- Ajustar fontes para Inter (ou usar SF Pro se for Mac)
- Exportar PNG 2x para web, 3x para print
