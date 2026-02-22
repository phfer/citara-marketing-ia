-- Migration: 003_create_core_tables.sql
-- Description: Criar tabelas core do sistema Citara Marketing IA
-- Author: @dev (Dex)
-- Date: 2026-02-22
-- Depends: 002_enable_rls.sql

-- ============================================================
-- TABELA 1: CLIENTES
-- ============================================================

CREATE TABLE clientes (
    id BIGSERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    ticket_mensal DECIMAL(10,2),
    status TEXT DEFAULT 'ativo' CHECK (status IN ('ativo', 'inativo', 'pausado')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

COMMENT ON TABLE clientes IS 'Clientes da agência de marketing';
COMMENT ON COLUMN clientes.nome IS 'Nome do cliente';
COMMENT ON COLUMN clientes.ticket_mensal IS 'Valor mensal do contrato (BRL)';
COMMENT ON COLUMN clientes.status IS 'Status: ativo, inativo ou pausado';

-- ============================================================
-- TABELA 2: PROJETOS
-- ============================================================

CREATE TABLE projetos (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT NOT NULL REFERENCES clientes(id) ON DELETE CASCADE,
    nome TEXT NOT NULL,
    tipo TEXT,
    status TEXT DEFAULT 'pendente' CHECK (status IN ('pendente', 'em_andamento', 'concluido', 'cancelado')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

COMMENT ON TABLE projetos IS 'Projetos de marketing por cliente';
COMMENT ON COLUMN projetos.cliente_id IS 'FK para cliente (CASCADE delete)';
COMMENT ON COLUMN projetos.tipo IS 'Tipo de projeto (ex: social_media, trafego_pago)';
COMMENT ON COLUMN projetos.status IS 'Status do projeto';

-- ============================================================
-- TABELA 3: CONTEÚDOS
-- ============================================================

CREATE TABLE conteudos (
    id BIGSERIAL PRIMARY KEY,
    projeto_id BIGINT NOT NULL REFERENCES projetos(id) ON DELETE CASCADE,
    tipo TEXT NOT NULL,
    plataforma TEXT,
    status TEXT DEFAULT 'rascunho' CHECK (status IN ('rascunho', 'revisao', 'aprovado', 'publicado')),
    url TEXT,
    titulo TEXT,
    descricao TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    publicado_at TIMESTAMPTZ
);

COMMENT ON TABLE conteudos IS 'Conteúdos de marketing (posts, artes, vídeos)';
COMMENT ON COLUMN conteudos.tipo IS 'Tipo: post, historia, reel, arte, video';
COMMENT ON COLUMN conteudos.plataforma IS 'Plataforma: instagram, facebook, linkedin, tiktok';
COMMENT ON COLUMN conteudos.status IS 'Status do conteúdo';
COMMENT ON COLUMN conteudos.url IS 'URL do conteúdo publicado';

-- ============================================================
-- TABELA 4: USUÁRIOS
-- ============================================================

CREATE TABLE usuarios (
    id BIGSERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT DEFAULT 'usuario' CHECK (role IN ('admin', 'usuario')),
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    last_login TIMESTAMPTZ
);

COMMENT ON TABLE usuarios IS 'Usuários do sistema';
COMMENT ON COLUMN usuarios.email IS 'Email único (login)';
COMMENT ON COLUMN usuarios.role IS 'Role: admin ou usuario';
COMMENT ON COLUMN usuarios.ativo IS 'Usuário ativo no sistema?';

-- ============================================================
-- HABILITAR RLS EM TODAS AS TABELAS
-- ============================================================

ALTER TABLE clientes ENABLE ROW LEVEL SECURITY;
ALTER TABLE projetos ENABLE ROW LEVEL SECURITY;
ALTER TABLE conteudos ENABLE ROW LEVEL SECURITY;
ALTER TABLE usuarios ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- CRIAR POLICIES RLS
-- ============================================================

-- Clientes: authenticated pode ler, admin pode tudo
CREATE POLICY "clientes_select_authenticated" ON clientes
    FOR SELECT TO authenticated USING (true);

CREATE POLICY "clientes_all_admin" ON clientes
    FOR ALL TO authenticated
    USING (auth.jwt() ->> 'role' = 'admin')
    WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- Projetos: authenticated pode ler, admin pode tudo
CREATE POLICY "projetos_select_authenticated" ON projetos
    FOR SELECT TO authenticated USING (true);

CREATE POLICY "projetos_all_admin" ON projetos
    FOR ALL TO authenticated
    USING (auth.jwt() ->> 'role' = 'admin')
    WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- Conteúdos: authenticated pode ler, admin pode tudo
CREATE POLICY "conteudos_select_authenticated" ON conteudos
    FOR SELECT TO authenticated USING (true);

CREATE POLICY "conteudos_all_admin" ON conteudos
    FOR ALL TO authenticated
    USING (auth.jwt() ->> 'role' = 'admin')
    WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- Usuários: usuário só vê seus dados, admin vê todos
CREATE POLICY "usuarios_select_self" ON usuarios
    FOR SELECT TO authenticated
    USING (email = (auth.jwt() ->> 'email'));

CREATE POLICY "usuarios_all_admin" ON usuarios
    FOR ALL TO authenticated
    USING (auth.jwt() ->> 'role' = 'admin')
    WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- ============================================================
-- CRIAR ÍNDICES BÁSICOS
-- ============================================================

-- Índices para performance
CREATE INDEX idx_clientes_status ON clientes(status);
CREATE INDEX idx_projetos_cliente_id ON projetos(cliente_id);
CREATE INDEX idx_projetos_status ON projetos(status);
CREATE INDEX idx_conteudos_projeto_id ON conteudos(projeto_id);
CREATE INDEX idx_conteudos_status ON conteudos(status);
CREATE INDEX idx_conteudos_plataforma ON conteudos(plataforma);
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_usuarios_role ON usuarios(role);

-- ============================================================
-- TRIGGERS PARA updated_at AUTOMÁTICO
-- ============================================================

-- Função para atualizar updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para clientes
CREATE TRIGGER update_clientes_updated_at
    BEFORE UPDATE ON clientes
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Trigger para projetos
CREATE TRIGGER update_projetos_updated_at
    BEFORE UPDATE ON projetos
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Trigger para conteudos
CREATE TRIGGER update_conteudos_updated_at
    BEFORE UPDATE ON conteudos
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Trigger para usuarios
CREATE TRIGGER update_usuarios_updated_at
    BEFORE UPDATE ON usuarios
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
