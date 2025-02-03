# HR_Reduction

#Dokumentacja:

# Dokumentacja Modeli Danych i Funkcji Pomocniczych

## Opis  
Kod definiuje struktury tabel oraz funkcje pomocnicze do obsługi bazy danych w systemie rekrutacyjnym.  
Wykorzystuje SQLAlchemy jako ORM (Object-Relational Mapping) do interakcji z bazą danych.

---
## Jak uruchomić?
Środowisko: Visual Studio 2022 (Python 3.11 | 64-bit)

1) Upewnij się że posiadasz wszystkie niezbędne pakiety (Main/requirements.txt)
2) Wykonaj querry na Bazie danych (plik DB_Insert/Scripts/DB_script.sql)
3) Podmień link do swerwera SQL (plik DB_Insert/Config/DataBase)
![image](https://github.com/user-attachments/assets/549786c8-9718-45bf-a3f8-5106aad5ceb0)
4) Uruchom Projekt DB_Insert i poczekaj aż wszystkie dane zostaną załadowane
5) Uruchom Projekt Main 

---
## Struktura Bazy Danych
![image](https://github.com/user-attachments/assets/f222dc8f-96e9-4a5f-964e-15df97c30e1b)

## Struktura Modeli Danych  

### 1. Model `Skill`  
Przechowuje informacje o umiejętnościach wymaganych przez oferty pracy oraz posiadanych przez kandydatów.  

- `skill_id` – Unikalny identyfikator umiejętności (klucz główny).  
- `skill_name` – Nazwa umiejętności (unikalna).  

---

### 2. Model `Applicant`  
Reprezentuje kandydatów aplikujących na oferty pracy.  

- `applicant_id` – Unikalny identyfikator kandydata (klucz główny).  
- `applicant_name` – Imię i nazwisko kandydata.  
- `industry` – Branża, w której kandydat pracuje.  
- `functional_area` – Obszar funkcjonalny stanowiska kandydata.  
- `experience` – Liczba lat doświadczenia.  
- `expected_salary` – Oczekiwana pensja kandydata.  

---

### 3. Model `ApplicantSkill`  
Łączy kandydatów z ich umiejętnościami (relacja wiele-do-wielu).  

- `applicant_id` – Odwołanie do kandydata.  
- `skill_id` – Odwołanie do umiejętności.  

---

### 4. Model `JobOffer`  
Przechowuje informacje o ofertach pracy publikowanych przez firmy.  

- `job_offer_id` – Unikalny identyfikator oferty pracy (klucz główny).  
- `job_title` – Nazwa stanowiska.  
- `role_category` – Kategoria roli.  
- `location` – Lokalizacja pracy.  
- `functional_area` – Obszar funkcjonalny stanowiska.  
- `industry` – Branża.  
- `salary` – Oferowane wynagrodzenie.  
- `required_experience` – Wymagane lata doświadczenia.  

---

### 5. Model `JobOfferSkill`  
Łączy oferty pracy z wymaganymi umiejętnościami (relacja wiele-do-wielu).  

- `job_offer_id` – Powiązanie z ofertą pracy.  
- `skill_id` – Powiązanie z wymaganymi umiejętnościami.  

---

### 6. Model `Application`  
Przechowuje aplikacje kandydatów na oferty pracy.  

- `applicant_id` – Kandydat aplikujący na ofertę.  
- `job_offer_id` – Oferta pracy, na którą kandydat aplikował.  

---

## Jak to działa?

### 1. Pobieranie szczegółów oferty pracy  
**Funkcja:** `get_job_offer_details(job_offer_id)`  

- Pobiera szczegóły konkretnej oferty pracy na podstawie jej ID.  
- Wykonuje zapytanie SQL, aby pobrać pełne dane oferty.  
- Zwraca listę słowników, gdzie każdy słownik reprezentuje jedną ofertę.  

---

### 2. Pobieranie wymaganych umiejętności dla oferty  
**Funkcja:** `get_required_skills(job_offer_id)`  

- Pobiera nazwy umiejętności wymaganych dla danej oferty.  
- Wykonuje zapytanie SQL z dołączeniem do tabeli `skills`.  
- Zwraca listę nazw umiejętności jako wartości tekstowe.  

---

### 3. Pobieranie kandydatów spełniających wymagania oferty  
**Funkcja:** `get_matching_applicants(job_offer_id)`  

- Pobiera listę kandydatów, którzy aplikowali na daną ofertę pracy.  
- Zawiera ich imię, doświadczenie, oczekiwaną pensję oraz wszystkie posiadane umiejętności.  
- Grupuje dane według kandydatów i zwraca je w formie listy słowników.  

---

## Podsumowanie  
Kod definiuje pełną strukturę danych oraz kluczowe funkcje pobierania informacji o ofertach, umiejętnościach i kandydatach.  
Jest to wydajny model ORM zoptymalizowany pod kątem systemu rekrutacyjnego, umożliwiający szybkie pobieranie i analizowanie danych.



# Heatmapa Dopasowania Umiejętności - Przegląd Dokumentacji

## Opis  
Heatmapa dopasowania umiejętności to wizualna reprezentacja, która pozwala na ocenę zgodności umiejętności kandydatów z wymaganiami określonej oferty pracy.  
Dzięki temu narzędziu rekruterzy mogą szybko zidentyfikować braki kompetencyjne lub mocne strony poszczególnych kandydatów.

Mapa przedstawia kandydatów (wiersze) oraz wymagane umiejętności (kolumny), a intensywność koloru wskazuje, czy kandydat posiada daną umiejętność.  
Zastosowanie heatmapy usprawnia analizę dopasowania profilu kandydatów do ofert pracy.

---

## Jak to działa?

### 1. Przygotowanie danych
- Funkcja pobiera kandydatów spełniających określone kryteria (doświadczenie, oczekiwana pensja, zgodność umiejętności).
- Pole `skill_name` każdego kandydata jest dzielone na pojedyncze umiejętności i przechowywane jako zbiór (set).
- Następnie funkcja iteruje przez wymagane umiejętności i sprawdza, czy dany kandydat je posiada.
- Jeśli kandydat posiada określoną umiejętność, wartość w komórce wynosi `1` (zostaje podświetlona kolorem).
- Jeśli kandydat nie posiada umiejętności, wartość komórki wynosi `0` (pozostaje jasna lub nie jest wypełniona).

---

### 2. Generowanie heatmapy
- Tworzenie **DataFrame** Pandas, gdzie:  
  - Wiersze reprezentują kandydatów.  
  - Kolumny odpowiadają wymaganym umiejętnościom.  
  - Wartości `1` i `0` określają, czy kandydat posiada daną umiejętność.  

- DataFrame jest przekazywany do funkcji **heatmap()** z biblioteki Seaborn,  
  która wizualizuje dopasowanie umiejętności przy użyciu palety kolorów `"YlGnBu"`.  

- Jeśli dane wejściowe są puste (brak kandydatów lub brak umiejętności),  
  generowana jest domyślna heatmapa z komunikatem `"Brak danych"`.

- Wygenerowana heatmapa jest:  
  - Zapisywana jako obraz w pamięci,  
  - Konwertowana na format **Base64**,  
  - Przekazywana do raportu internetowego jako obraz do wyświetlenia.

---

## Zastosowanie
- Umożliwia szybkie porównanie kandydatów pod kątem kluczowych umiejętności.  
- Pomaga w podejmowaniu decyzji o rekrutacji na podstawie zgodności kompetencyjnej.  
- Stanowi wartościowe narzędzie analityczne dla działów HR i menedżerów rekrutacyjnych.



