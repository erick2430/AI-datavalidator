"""
AI STUDY COACH - PROJECT 2: Data Validator with Machine Learning Preview
Teaches: Functions, Data Structures, Pattern Recognition, File I/O
"""

import re
import json
import csv
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# ==================== CORE VALIDATION FUNCTIONS ====================

def validate_email(email: str) -> Tuple[bool, str]:
    """Validate email format with multiple verification levels."""
    # Basic pattern matching (Rule-based AI concept)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False, "Invalid email format"
    
    # Simulate ML-based validation (preview!)
    suspicious_patterns = ['spam', 'fake', 'test', 'temp']
    if any(pattern in email.lower() for pattern in suspicious_patterns):
        return False, "Email appears suspicious"
    
    return True, "Valid email"

def validate_password(password: str, min_length: int = 8) -> Dict:
    """
    Password validator with security scoring.
    Returns detailed analysis (like ML model predictions).
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= min_length:
        score += 25
    else:
        feedback.append(f"Password should be at least {min_length} characters")
    
    # Check complexity (like feature engineering)
    checks = {
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    for check_name, passed in checks.items():
        if passed:
            score += 18.75  # 75/4 = 18.75 per check
        else:
            feedback.append(f"Add at least one {check_name} character")
    
    # AI-like pattern detection
    common_patterns = ['123456', 'password', 'qwerty', 'admin']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 30
        feedback.append("Avoid common password patterns")
    
    # Security rating (classification concept)
    if score >= 90:
        rating = "Excellent"
    elif score >= 70:
        rating = "Good"
    elif score >= 50:
        rating = "Fair"
    else:
        rating = "Weak"
    
    return {
        'score': score,
        'rating': rating,
        'feedback': feedback,
        'checks_passed': sum(checks.values()),
        'total_checks': len(checks)
    }

def validate_date(date_str: str, format: str = "%Y-%m-%d") -> Tuple[bool, Optional[datetime]]:
    """Date validator that returns both boolean and parsed date."""
    try:
        parsed_date = datetime.strptime(date_str, format)
        
        # Business logic validation (future dates not allowed)
        if parsed_date > datetime.now():
            return False, None
        
        return True, parsed_date
    except ValueError:
        return False, None

def validate_phone(phone: str) -> bool:
    """Validate international phone numbers."""
    # Remove all non-digits
    digits = re.sub(r'\D', '', phone)
    
    # Valid if between 10-15 digits
    return 10 <= len(digits) <= 15

# ==================== DATA PROCESSING PIPELINE ====================

class DataValidator:
    """Mimics an ML pipeline - processes batches of data."""
    
    def __init__(self):
        self.validation_rules = {
            'email': validate_email,
            'password': validate_password,
            'date': validate_date,
            'phone': validate_phone
        }
        self.stats = {'total': 0, 'passed': 0, 'failed': 0}
    
    def process_batch(self, data: List[Dict]) -> List[Dict]:
        """Process multiple records at once (like batch processing in ML)."""
        results = []
        
        for record in data:
            validated_record = self._validate_record(record)
            results.append(validated_record)
            
            # Update statistics
            self.stats['total'] += 1
            if all(r['valid'] for r in validated_record.values()):
                self.stats['passed'] += 1
            else:
                self.stats['failed'] += 1
        
        return results
    
    def _validate_record(self, record: Dict) -> Dict:
        """Validate a single record."""
        validated = {}
        
        for field, value in record.items():
            if field in self.validation_rules:
                validator = self.validation_rules[field]
                
                if field == 'password':
                    result = validator(value)
                    validated[field] = {
                        'valid': result['score'] >= 50,
                        'details': result
                    }
                else:
                    is_valid, details = validator(value) if field == 'email' else (validator(value), None)
                    validated[field] = {
                        'valid': is_valid,
                        'details': details
                    }
        
        return validated
    
    def get_statistics(self) -> Dict:
        """Return validation statistics."""
        if self.stats['total'] == 0:
            return self.stats
        
        self.stats['pass_rate'] = (self.stats['passed'] / self.stats['total']) * 100
        return self.stats

# ==================== FILE HANDLING (DATA LOADING) ====================

def load_csv_data(filename: str) -> List[Dict]:
    """Load data from CSV file (common in ML)."""
    data = []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        print(f"✅ Loaded {len(data)} records from {filename}")
    except FileNotFoundError:
        print(f"⚠️  File {filename} not found. Using sample data.")
        # Fallback to sample data
        data = [
            {'email': 'user1@example.com', 'password': 'Pass123!', 'date': '2023-01-15', 'phone': '123-456-7890'},
            {'email': 'invalid-email', 'password': 'weak', 'date': '2025-01-01', 'phone': '123'},
            {'email': 'spam@fake.com', 'password': 'StrongPass!2023', 'date': '2022-12-31', 'phone': '+1-234-567-8900'}
        ]
    
    return data

def save_results(results: List[Dict], filename: str = 'validation_results.json'):
    """Save validation results (like saving model outputs)."""
    with open(filename, 'w') as file:
        json.dump(results, file, indent=2, default=str)
    print(f"💾 Results saved to {filename}")

# ==================== ADVANCED: PATTERN DETECTION ====================

def detect_data_patterns(data: List[Dict]) -> Dict:
    """Simple pattern detection (AI concept preview)."""
    if not data:
        return {}
    
    patterns = {
        'email_domains': {},
        'password_lengths': [],
        'date_range': {'min': None, 'max': None}
    }
    
    for record in data:
        # Count email domains
        if 'email' in record:
            email = record['email']
            if '@' in email:
                domain = email.split('@')[1]
                patterns['email_domains'][domain] = patterns['email_domains'].get(domain, 0) + 1
        
        # Analyze password lengths
        if 'password' in record:
            patterns['password_lengths'].append(len(record['password']))
    
    # Calculate statistics (basic data analysis)
    if patterns['password_lengths']:
        patterns['password_stats'] = {
            'avg_length': sum(patterns['password_lengths']) / len(patterns['password_lengths']),
            'min_length': min(patterns['password_lengths']),
            'max_length': max(patterns['password_lengths'])
        }
    
    return patterns

# ==================== MAIN EXECUTION ====================

def main():
    """Main pipeline - this mimics an ML training/evaluation pipeline."""
    print("=" * 60)
    print("🤖 AI DATA VALIDATION PIPELINE")
    print("=" * 60)
    
    # 1. Load data (like loading training data)
    print("\n📂 PHASE 1: Data Loading")
    data = load_csv_data('user_data.csv')  # Try to load from file
    
    # 2. Initialize validator (like initializing a model)
    print("\n🔧 PHASE 2: Initialize Validator")
    validator = DataValidator()
    
    # 3. Process batch (like model training/prediction)
    print("\n⚙️  PHASE 3: Batch Processing")
    results = validator.process_batch(data)
    
    # 4. Show results
    print("\n📊 PHASE 4: Results")
    for i, result in enumerate(results, 1):
        print(f"\nRecord {i}:")
        for field, validation in result.items():
            status = "✅" if validation['valid'] else "❌"
            print(f"  {field}: {status}")
            if 'details' in validation and validation['details']:
                if isinstance(validation['details'], dict):
                    for key, value in validation['details'].items():
                        print(f"    {key}: {value}")
    
    # 5. Statistics
    print("\n📈 PHASE 5: Statistics")
    stats = validator.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # 6. Pattern detection (AI preview)
    print("\n🔍 PHASE 6: Pattern Detection (AI Preview)")
    patterns = detect_data_patterns(data)
    print(f"  Email domains found: {len(patterns.get('email_domains', {}))}")
    if 'password_stats' in patterns:
        print(f"  Average password length: {patterns['password_stats']['avg_length']:.1f}")
    
    # 7. Save results
    print("\n💾 PHASE 7: Save Results")
    save_results({
        'validation_results': results,
        'statistics': stats,
        'patterns': patterns
    })
    
    print("\n" + "=" * 60)
    print("🎯 DAY 2 COMPLETE!")
    print("=" * 60)

# ==================== CHALLENGES ====================

def challenge_1():
    """Add a new validation rule for usernames."""
    # Requirements: 3-20 chars, alphanumeric only
    pass

def challenge_2():
    """Create a function that generates synthetic test data."""
    # Generate 100 fake records for testing
    pass

def challenge_3():
    """Add data visualization to show validation statistics."""
    # Use matplotlib to create a bar chart of pass/fail rates
    pass

if __name__ == "__main__":
    main()