IF NOT EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'HR_Reduction')
BEGIN
    CREATE DATABASE HR_Reduction;
END;
USE HR_Reduction;

-- Czyszczenie tabel
IF OBJECT_ID('job_offer_skills', 'U') IS NOT NULL DROP TABLE job_offer_skills;
IF OBJECT_ID('applicant_skills', 'U') IS NOT NULL DROP TABLE applicant_skills;
IF OBJECT_ID('applications', 'U') IS NOT NULL DROP TABLE applications;
IF OBJECT_ID('skills', 'U') IS NOT NULL DROP TABLE skills;
IF OBJECT_ID('job_offers', 'U') IS NOT NULL DROP TABLE job_offers;
IF OBJECT_ID('applicants', 'U') IS NOT NULL DROP TABLE applicants;

-- Tabela: job_offers
CREATE TABLE job_offers (
    job_offer_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    job_title NVARCHAR(255) NOT NULL,
    role_category NVARCHAR(255),
    location NVARCHAR(255),
    functional_area NVARCHAR(255),
    industry NVARCHAR(255),
    salary FLOAT CHECK (salary >= 0),
    required_experience INT CHECK (required_experience >= 0)
);

-- Tabela: skills
CREATE TABLE skills ( 
    skill_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    skill_name NVARCHAR(255) NOT NULL UNIQUE
);

-- Tabela: job_offer_skills
CREATE TABLE job_offer_skills (
    job_offer_id BIGINT NOT NULL,
    skill_id BIGINT NOT NULL,
    PRIMARY KEY (job_offer_id, skill_id),
    FOREIGN KEY (job_offer_id) REFERENCES job_offers(job_offer_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id) ON DELETE CASCADE
);

-- Tabela: applicants
CREATE TABLE applicants (
    applicant_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    applicant_name NVARCHAR(255) NOT NULL,
    industry NVARCHAR(255),
    functional_area NVARCHAR(255),
    experience INT NOT NULL,
    expected_salary FLOAT NOT NULL
);

-- Tabela: applicant_skills
CREATE TABLE applicant_skills (
    applicant_id BIGINT NOT NULL,
    skill_id BIGINT NOT NULL,
    PRIMARY KEY (applicant_id, skill_id),
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id) ON DELETE CASCADE
);

-- Tabela: applications
CREATE TABLE applications ( 
    applicant_id BIGINT NOT NULL,
    job_offer_id BIGINT NOT NULL,
	PRIMARY KEY (applicant_id, job_offer_id),
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id) ON DELETE CASCADE,
    FOREIGN KEY (job_offer_id) REFERENCES job_offers(job_offer_id) ON DELETE CASCADE
);

