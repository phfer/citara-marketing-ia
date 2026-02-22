-- Migration: 002_enable_rls.sql
-- Description: Habilitar Row Level Security em todas as tabelas
-- Author: @dev (Dex)
-- Date: 2026-02-22
-- Depends: 001_revoke_generic_grants.sql

-- ⚠️ IMPORTANTE: RLS será habilitado, mas policies devem ser criadas
-- ANTES de habilitar para não bloquear todo acesso.

-- Nota: Como as tabelas ainda não existem (serão criadas em STORY-1.2),
-- esta migration documenta o processo. RLS será habilitado na criação
-- de cada tabela.

-- Exemplo do padrão a seguir em cada tabela:

-- 1. Habilitar RLS na tabela
-- ALTER TABLE nome_tabela ENABLE ROW LEVEL SECURITY;

-- 2. Criar policy para leitura (authenticated)
-- CREATE POLICY " nome_tabela_select_authenticated"
--   ON nome_tabela FOR SELECT
--   TO authenticated
--   USING (true);

-- 3. Criar policy para escrita (admin apenas)
-- CREATE POLICY "nome_tabela_write_admin"
--   ON nome_tabela FOR ALL
--   TO authenticated
--   USING (
--     auth.jwt() ->> 'role' = 'admin'
--   )
--   WITH CHECK (
--     auth.jwt() ->> 'role' = 'admin'
--   );

-- 4. Criar policy para leitura pública (se aplicável)
-- CREATE POLICY "nome_tabela_select_anon"
--   ON nome_tabela FOR SELECT
--   TO anon
--   USING (true);

-- ============================================================
-- POLICIES POR TABELA (serão aplicadas em STORY-1.2)
-- ============================================================

-- Tabela: clientes
-- ALTER TABLE clientes ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "clientes_select_authenticated" ON clientes
--   FOR SELECT TO authenticated USING (true);
-- CREATE POLICY "clientes_all_admin" ON clientes
--   FOR ALL TO authenticated
--   USING (auth.jwt() ->> 'role' = 'admin')
--   WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- Tabela: projetos
-- ALTER TABLE projetos ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "projetos_select_authenticated" ON projetos
--   FOR SELECT TO authenticated USING (true);
-- CREATE POLICY "projetos_all_admin" ON projetos
--   FOR ALL TO authenticated
--   USING (auth.jwt() ->> 'role' = 'admin')
--   WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- Tabela: conteudos
-- ALTER TABLE conteudos ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "conteudos_select_authenticated" ON conteudos
--   FOR SELECT TO authenticated USING (true);
-- CREATE POLICY "conteudos_all_admin" ON conteudos
--   FOR ALL TO authenticated
--   USING (auth.jwt() ->> 'role' = 'admin')
--   WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- Tabela: usuarios
-- ALTER TABLE usuarios ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "usuarios_select_self" ON usuarios
--   FOR SELECT TO authenticated
--   USING (auth.uid() = id);
-- CREATE POLICY "usuarios_all_admin" ON usuarios
--   FOR ALL TO authenticated
--   USING (auth.jwt() ->> 'role' = 'admin')
--   WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- ============================================================
-- VALIDAÇÃO
-- ============================================================

-- Para verificar se RLS está ativo:
-- SELECT tablename, rowsecurity
-- FROM pg_tables
-- WHERE schemaname = 'public';

-- Para verificar policies de uma tabela:
-- SELECT schemaname, tablename, policyname, permissive, roles, cmd, qual
-- FROM pg_policies
-- WHERE schemaname = 'public';

-- ============================================================
-- NOTAS IMPORTANTES
-- ============================================================

-- 1. RLS deve ser habilitado APÓS criar as tabelas
-- 2. Policies devem ser criadas ANTES de habilitar RLS
-- 3. A política acima usa 'admin' como role administrativo
-- 4. Ajuste o role conforme sua autenticação (auth.jwt() ->> 'role')
-- 5. Para Supabase Auth, use auth.uid() para comparar com user_id
