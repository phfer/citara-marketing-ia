-- Migration: 001_revoke_generic_grants.sql
-- Description: Revogar permissões genéricas GRANT ALL (DB-003)
-- Author: @dev (Dex)
-- Date: 2026-02-22

-- ⚠️ CRÍTICO: Esta migration deve ser executada ANTES de habilitar RLS
-- para não perder acesso administrativo.

-- 1. Revoke permissões genéricas de anon (público)
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM anon;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM anon;
REVOKE ALL ON ALL FUNCTIONS IN SCHEMA public FROM anon;

-- 2. Revoke permissões genéricas de authenticated
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM authenticated;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM authenticated;
REVOKE ALL ON ALL FUNCTIONS IN SCHEMA public FROM authenticated;

-- 3. Revoke permissões genéricas de service_role
-- (service_role manterá permissões administrativas)
-- REVOKE ALL ON ALL TABLES IN SCHEMA public FROM service_role;
-- REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM service_role;
-- REVOKE ALL ON ALL FUNCTIONS IN SCHEMA public FROM service_role;

-- 4. Conceder permissões mínimas para USAGE (conectar ao schema)
-- Estas são permissões inofensivas que apenas permitem conectar
GRANT USAGE ON SCHEMA public TO anon, authenticated, service_role;

-- 5. Conceder permissão de SELECT em tabelas para anon (leitura pública)
-- Será refinado quando tabelas existirem com RLS
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO anon;

-- 6. Conceder permissões básicas para authenticated
-- Será refinado quando tabelas existirem com RLS
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO authenticated;
-- GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO authenticated;
-- GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO authenticated;

-- Nota: As permissões específicas por tabela serão definidas
-- nas migrations de criação de tabelas (STORY-1.2)
