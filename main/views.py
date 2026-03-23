from django.shortcuts import render

def build_portfolio_context():
    return {
        'name': 'Himanshu Agnihotri',
        'email': 'himanshuagnihotrivb@gmail.com',
        'phone': '+91 8923591490',
        'linkedin': 'https://www.linkedin.com/in/himanshuagnihotri5623/',
        'github': 'https://github.com/Himanshu5623',
        'location': 'Hathras, Uttar Pradesh, India',
        'hero_title': 'AI & ML-focused Computer Science student building practical, data-driven web products.',
        'hero_summary': (
            'I am a Computer Science student specializing in Artificial Intelligence and Machine Learning, '
            'with hands-on experience in Data Science, Predictive Modeling, and Natural Language Processing. '
            'I work with Python, SQL, Scikit-learn, Pandas, and NumPy to build machine learning solutions '
            'and data-driven systems.'
        ),
        'focus_areas': [
            'Production-ready ML systems with real-world data',
            'AI-powered web apps with user-friendly interfaces',
            'Predictive analytics and NLP solutions',
            'Full-stack data projects from analysis to deployment',
        ],
        'stats': [
            {'value': '3+', 'label': 'AI and data projects built'},
            {'value': '10+', 'label': 'certifications completed'},
            {'value': '2', 'label': 'degrees completed / in progress'},
        ],
        'about_points': [
            'I am a Computer Science student specializing in Artificial Intelligence and Machine Learning, with hands-on experience in Data Science, Predictive Modeling, and Natural Language Processing.',
            'I work with Python, SQL, Scikit-learn, Pandas, and NumPy to build machine learning solutions, perform exploratory data analysis, and develop end-to-end data-driven systems.',
            'My projects include sentiment analysis, predictive analytics, and PathVera, an AI-powered career coach platform that analyzes job market trends and recommends skills and career paths.',
            'I am actively seeking opportunities in Data Science, Machine Learning, AI/ML research, and data-focused roles where I can apply and grow my skills.',
        ],
        'education': [
            {
                'institution': 'Lovely Professional University',
                'location': 'Phagwara, Punjab',
                'program': 'Bachelor of Technology in Computer Science and Engineering (AI & ML)',
                'score': 'CGPA: 6.74',
                'duration': 'Aug 2024 - Jul 2027',
            },
            {
                'institution': 'Mangalayatan University',
                'location': 'Aligarh, Uttar Pradesh',
                'program': 'Diploma in Computer Science and Engineering',
                'score': 'CGPA: 8.32',
                'duration': 'Aug 2021 - Jul 2024',
            },
            {
                'institution': 'St. Francis Inter College',
                'location': 'Hathras, Uttar Pradesh',
                'program': 'Matriculation',
                'score': 'Percentage: 69%',
                'duration': 'Mar 2020 - May 2021',
            },
        ],
        'training': {
            'title': 'Fundamentals of Data Structures: Learn, Apply and Build Projects',
            'provider': 'Lovely Professional University',
            'duration': 'Jun 2025 - Jul 2025',
            'url': 'https://drive.google.com/file/d/1H-1dcg5acFg8LtLe8t5Wh_dc8GvS-REB/view?usp=drive_link',
            'details': [
                'Implemented arrays, linked lists, stacks, queues, hash tables, trees, and graphs to solve computational problems.',
                'Applied sorting and searching techniques including Merge Sort, Quick Sort, Heap Sort, and Binary Search.',
                'Strengthened algorithmic thinking by optimizing solutions through hands-on coding practice.',
            ],
        },
        'projects': [
            {
                'title': 'PathVera',
                'subtitle': 'AI-Powered Career Recommendation System',
                'duration': 'Feb 2026',
                'desc': 'Built a full-stack recommendation platform that parses resumes, matches candidate profiles to career paths, and surfaces job-market context.',
                'impact': 'Resume intelligence, semantic matching, and career guidance in one product flow.',
                'cover_tag': 'NLP + Career AI',
                'cover_kicker': 'Transformer-assisted recommendations',
                'theme': 'sunrise',
                'github_url': 'https://github.com/Himanshu5623/PathVera',
                'highlights': [
                    'Created an NLP-driven resume parsing pipeline for extracting skills, education, and experience from PDF and DOCX files.',
                    'Implemented semantic matching with transformer embeddings and cosine similarity for role recommendations.',
                    'Connected O*NET role mapping and Adzuna API data for skill-gap analysis, salary insight, and real-time job context.',
                ],
                'tech': 'Python, Django, HTML/CSS, JavaScript, Sentence-Transformers, SQLite, NumPy, Chart.js',
            },
            {
                'title': 'Sentiment Analysis of Social Media Presence',
                'subtitle': 'Social media comment analysis pipeline',
                'duration': 'Dec 2025',
                'desc': 'Explored sentiment trends and engagement behavior in YouTube comment data using NLP preprocessing and supervised ML models.',
                'impact': 'Turns noisy social discussion into measurable sentiment and engagement signals.',
                'cover_tag': 'Data + Sentiment',
                'cover_kicker': 'From raw comments to structured insight',
                'theme': 'forest',
                'github_url': 'https://github.com/Himanshu5623/-Sentiment-Analysis-of-Social-Media-Presence',
                'highlights': [
                    'Performed exploratory analysis to uncover sentiment patterns, engagement peaks, and comment behavior correlations.',
                    'Structured transformer-processed comment data into a cleaner dataset for downstream sentiment classification.',
                    'Trained TF-IDF-based models and evaluated performance with accuracy, precision, and recall metrics.',
                ],
                'tech': 'Python, Pandas, NumPy, Transformers, Scikit-learn, Machine Learning',
            },
            {
                'title': 'AI Based Oxygen Level Detection on Heaters During Wintertime',
                'subtitle': 'IoT safety monitoring system',
                'duration': 'Apr 2025',
                'desc': 'Designed a smart monitoring system that predicts unsafe oxygen conditions near heaters using real-time sensor data and ML support.',
                'impact': 'Combines hardware sensing and machine learning for a safety-first user experience.',
                'cover_tag': 'IoT + Safety',
                'cover_kicker': 'Sensor-driven prediction interface',
                'theme': 'ember',
                'github_url': 'https://github.com/Himanshu5623/AI-Based-Oxygen-Level-Detection-System-for-Room-Heaters-',
                'highlights': [
                    'Worked with MQ-135, DHT22, and ESP32/Arduino components to gather environmental readings.',
                    'Processed live sensor data to estimate risk and trigger safety-focused alerts.',
                    'Built a Flask dashboard for showing readable real-time values and predictions to users.',
                ],
                'tech': 'Python, Flask, Machine Learning, ESP32/Arduino, IoT Sensors, HTML/CSS',
            }
        ],
        'skills': {
            'languages': [
                {'name': 'Python', 'icon': 'fa-brands fa-python'},
                {'name': 'Java', 'icon': 'fa-brands fa-java'},
                {'name': 'C', 'icon': 'fa-solid fa-code'},
                {'name': 'C++', 'icon': 'fa-solid fa-laptop-code'},
                {'name': 'HTML/CSS', 'icon': 'fa-brands fa-html5'},
                {'name': 'JavaScript', 'icon': 'fa-brands fa-js'},
            ],
            'frameworks': [
                {'name': 'Django', 'icon': 'fa-solid fa-layer-group'},
                {'name': 'Flask', 'icon': 'fa-solid fa-flask'},
                {'name': 'Scikit-learn', 'icon': 'fa-solid fa-brain'},
                {'name': 'Transformers (NLP)', 'icon': 'fa-solid fa-language'},
                {'name': 'Streamlit', 'icon': 'fa-solid fa-chart-line'},
                {'name': 'TensorFlow', 'icon': 'fa-solid fa-microchip'},
                {'name': 'Matplotlib', 'icon': 'fa-solid fa-chart-column'},
            ],
            'tools': [
                {'name': 'Git', 'icon': 'fa-brands fa-git-alt'},
                {'name': 'GitHub', 'icon': 'fa-brands fa-github'},
                {'name': 'MySQL', 'icon': 'fa-solid fa-database'},
                {'name': 'SQLite', 'icon': 'fa-solid fa-server'},
                {'name': 'NumPy', 'icon': 'fa-solid fa-square-root-variable'},
                {'name': 'Pandas', 'icon': 'fa-solid fa-table'},
                {'name': 'Chart.js', 'icon': 'fa-solid fa-chart-pie'},
            ],
            'soft_skills': [
                {'name': 'Collaborative mindset', 'icon': 'fa-solid fa-people-group'},
                {'name': 'Task management', 'icon': 'fa-solid fa-list-check'},
                {'name': 'Detail-oriented execution', 'icon': 'fa-solid fa-bullseye'},
                {'name': 'Effective communication', 'icon': 'fa-solid fa-comments'},
                {'name': 'Learning agility', 'icon': 'fa-solid fa-seedling'},
            ],
        },
        'certifications': [
            {
                'title': 'Advanced Statistics',
                'issuer': 'Simplilearn',
                'date': 'Jan 2026',
                'url': 'https://drive.google.com/file/d/1vncotda5bil7EsMDrIH3ASRqejTiG3EN/view?usp=sharing',
            },
            {
                'title': 'Workshop at AWS Student Community Day Jalandhar',
                'issuer': 'AWS',
                'date': 'Nov 2025',
                'url': 'https://drive.google.com/file/d/1yTsi-zttsmiNKeXHTRB3YKeQedmDe6ec/view?usp=drive_link',
            },
            {
                'title': 'Computational Theory: Language Principles & Finite Automata Theory',
                'issuer': 'Infosys Springboard',
                'date': 'Aug 2025',
                'url': 'https://drive.google.com/file/d/1gfxtrgLKAQrrcSD9sb3rMOy7DfdPMEIY/view?usp=drive_link',
            },
            {
                'title': 'Java Programming',
                'issuer': 'iamNeo',
                'date': 'May 2025',
                'url': 'https://drive.google.com/file/d/1sfc5OalJf1941Kz_QnzivP2z7XYHxBxN/view?usp=drive_link',
            },
            {
                'title': 'Data Structures and Algorithm',
                'issuer': 'iamNeo',
                'date': 'Dec 2024',
                'url': 'https://drive.google.com/file/d/1KqBEMXNLKNkpLvvNJ-bjbPSixjMPKwF7/view?usp=drive_link',
            },
            {
                'title': 'Object Oriented Programming',
                'issuer': 'iamNeo',
                'date': 'Dec 2024',
                'url': 'https://drive.google.com/file/d/1pXIbBfu2hOkIxBt9nJgKgUFCZIrjKyDy/view?usp=drive_link',
            },
            {
                'title': 'Packet Switching Networks and Algorithms',
                'issuer': 'Coursera',
                'date': 'Nov 2024',
                'url': 'https://drive.google.com/file/d/1D38uf4QaRjKixvqcn_UYMw_mn7xi1Pcs/view?usp=drive_link',
            },
            {
                'title': 'Peer-to-Peer Protocols and Local Area Networks',
                'issuer': 'Coursera',
                'date': 'Oct 2024',
                'url': 'https://drive.google.com/file/d/1A2Kxxlwlh5PWx2w2VuIpLjEgF0EZzBtm/view?usp=drive_link',
            },
            {
                'title': 'The Bits and Bytes of Computer Networking',
                'issuer': 'Coursera',
                'date': 'Sep 2024',
                'url': 'https://drive.google.com/file/d/1SlG4B2NlRLl4-2gsb1-_9bf5F2GA7Hbb/view?usp=drive_link',
            },
            {
                'title': 'Fundamentals of Network Communication',
                'issuer': 'Coursera',
                'date': 'Sep 2024',
                'url': 'https://drive.google.com/file/d/1Y-oYbpNu48LqQ5IG-zEhnB6NbpUjZ2Gg/view?usp=sharing',
            },
        ],
    }


def home(request):
    context = build_portfolio_context()
    context.update({
        'page': 'home',
    })
    return render(request, 'index.html', context)


def about(request):
    context = build_portfolio_context()
    context.update({
        'page': 'about',
    })
    return render(request, 'about.html', context)


def skills(request):
    context = build_portfolio_context()
    context.update({
        'page': 'skills',
    })
    return render(request, 'skills.html', context)


def projects(request):
    context = build_portfolio_context()
    context.update({
        'page': 'projects',
    })
    return render(request, 'projects.html', context)


def custom_404(request, exception):
    context = build_portfolio_context()
    context.update({
        'page': '',
    })
    return render(request, '404.html', context, status=404)
