-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 30/10/2023 às 07:34
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `atividade_p4`
--
CREATE DATABASE IF NOT EXISTS `atividade_p4` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `atividade_p4`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `candidatos`
--

CREATE TABLE `candidatos` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  `minibio` varchar(150) DEFAULT NULL,
  `nota_entrevista` int(11) DEFAULT NULL,
  `nota_teorico` int(11) DEFAULT NULL,
  `nota_pratica` int(11) DEFAULT NULL,
  `nota_softskills` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `candidatos`
--

INSERT INTO `candidatos` (`id`, `nome`, `telefone`, `minibio`, `nota_entrevista`, `nota_teorico`, `nota_pratica`, `nota_softskills`) VALUES
(1, 'Luis Otavio Pais', '15981001090', 'Olá, tenho interesse em trabalhar na área de T.I', 9, 7, 8, 10),
(2, 'Fábio Deodato', '15999999999', 'Olá, tenho interesse em trabalhar na área da Logística', 7, 7, 8, 7),
(3, 'Gabriel Rodrigues', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 8, 8, 10, 7),
(4, 'Lucas Vieira', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 8, 9, 9, 8),
(5, 'Gabriel Flaise', '15999999999', 'Olá, tenho interesse em trabalhar na área de Mecânica', 9, 5, 10, 7),
(6, 'Ana Laura', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 7, 10, 10, 6),
(7, 'Jovelina Paes', '15999999999', 'olá, tenho interesse em atuar na área de enfermagem', 9, 8, 9, 8),
(8, 'Elisangela Paes', '15999999999', 'Olá, tenho interesse em atuar na área educacional', 9, 9, 8, 7),
(9, 'Vinicius Pantojo', '15999999999', 'olá, tenho interesse em atuar na área de logística', 8, 7, 9, 9),
(10, 'Lucas Souza', '15999999999', 'olá, tenho interesse em atuar na área do esporte', 9, 8, 8, 7),
(11, 'João Jesus', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 8, 9, 10, 7),
(12, 'Ruan Patrick', '15999999999', 'olá, tenho interesse em trabalhar na área de entrega', 9, 7, 8, 9),
(13, 'Glória Queiroz', '15999999999', 'Olá, tenho interesse em trabalhar na área de Compras', 9, 7, 6, 7),
(14, 'Maicon Douglas', '15999999999', 'Olá, tenho interesse em atuar na área de Mecância Automotiva', 6, 7, 6, 5),
(15, 'Adrian Roberto', '15999999999', 'Olá, tenho interesse em atuar na área de Esportes', 5, 6, 6, 4),
(16, 'Ana Julia', '15999999999', 'Olá, tenho interesse em atuar na área educacional', 9, 8, 7, 9),
(17, 'Giovanna Luvizoto', '15999999999', 'Olá, tenho interesse em atuar na área Administrativa', 8, 7, 8, 6),
(18, 'Ryan Hessel', '15999999999', 'Olá, tenho interesse em atuar na área Administrativa', 7, 7, 8, 8),
(19, 'Thiago Antunes', '15999999999', 'Olá, tenho interesse em atuar na área de T.I', 8, 8, 7, 8),
(20, 'Helena Camargo', '15999999999', 'Olá, tenho interesse em atuar na área de Vendas', 7, 6, 6, 8);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `candidatos`
--
ALTER TABLE `candidatos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `candidatos`
--
ALTER TABLE `candidatos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
