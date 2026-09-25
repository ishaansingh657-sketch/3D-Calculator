-- ============================================
-- 3D Scientific Calculator Database
-- ============================================

CREATE DATABASE IF NOT EXISTS calculator_db;

USE calculator_db;

-- ============================================
-- Calculator Settings
-- ============================================

CREATE TABLE IF NOT EXISTS calculator_settings (
    id INT NOT NULL AUTO_INCREMENT,
    decimal_places INT DEFAULT 10,
    angle_mode VARCHAR(20) DEFAULT 'DEG',
    theme VARCHAR(50) DEFAULT '3D Glass',
    PRIMARY KEY (id)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

-- ============================================
-- Default Calculator Settings
-- ============================================

INSERT INTO calculator_settings
    (decimal_places, angle_mode, theme)
VALUES
    (10, 'DEG', '3D Glass');