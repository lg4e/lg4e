# Markdown 渲染所需扩展
from markdown.extensions import fenced_code, tables

MARKDOWN_EXTENSIONS = [
    fenced_code.FencedCodeExtension(),
    tables.TableExtension()
]

# 默认模板文件
DEFAULT_404_TEMPLATE = "404.html"
DEFAULT_500_TEMPLATE = "500.html"

# 分类数据
CATEGORIES = {
    "set_theory_and_logic": {
        "title": "Set Theory and Logic",
        "description": "An introduction to Set Theory and Logic",
    },
    "formal_logic": {
        "title": "Formal Logic",
        "description": "An Introduction to Formal Logic",
    },
    "linear_algebra": {
        "title": "Linear Algebra",
        "description": "This card explores the foundational concepts of linear algebra.",
    },
    "calculus": {
        "title": "Calculus",
        "description": "This card focuses on the essential topics in calculus.",
    },
    "discrete_math": {
        "title": "Discrete Mathematics",
        "description": "This card covers fundamental topics in discrete math.",
    },
    "abstract_algebra": {
        "title": "Abstract Algebra",
        "description": "This card delves into groups, rings, and fields.",
    },
    "probability_theory": {
        "title": "Probability Theory",
        "description": "This card introduces key concepts in probability.",
    },
    "real_analysis": {
        "title": "Real Analysis",
        "description": "This card explores rigorous calculus topics.",
    },
    "computer_science_basics": {
        "title": "Computer Science Basics",
        "description": "This card introduces fundamental concepts in computer science.",
    },
    "graph_theory": {
        "title": "Graph Theory",
        "description": "This card dives into the structure and properties of graphs.",
    },
}

# 书籍数据
BOOKS = {
    "set_theory_and_logic": [
        {
            "slug": "general_topology",
            "title": "General Topology",
            "parts": {
                "I": {
                    "title": "Introduction to Topology",
                    "chapters": {
                        1: {
                            "title": "Foundations of Set Theory",
                            "sections": {
                                1: "Fundamental Concepts",
                                2: "Functions",
                                3: "Relations",
                            },
                        },
                    },
                },
            },
        },
        {
            "slug": "algebraic_topology",
            "title": "Algebraic Topology",
            "parts": {
                "I": {
                    "title": "Introduction to Algebraic Structures",
                    "chapters": {
                        2: {
                            "title": "Number Systems and Cartesian Products",
                            "sections": {
                                1: "The Integers and the Real Numbers",
                                2: "Cartesian Products",
                            },
                        },
                        3: {
                            "title": "Advanced Topics in Set Theory",
                            "sections": {
                                1: "Finite Sets",
                                2: "Countable and Uncountable Sets",
                                3: "The Principle of Recursive Definition",
                                4: "Infinite Sets and the Axiom of Choice",
                                5: "Well-Ordered Sets",
                            },
                        },
                    },
                },
            },
        },
    ],
    "formal_logic": [
        {
            "slug": "forallxyyc",
            "title": "forallxyyc",
            "parts": {
                "I": {
                    "title": "Key Notions of Logic",
                    "chapters": {
                        1: {
                            "title": "Arguments",
                            "sections": {
                                1: "The Foundations of Logical Reasoning",
                                2: "Principles of Deductive and Inductive Logic",
                                3: "Logical Fallacies: Identifying Errors in Arguments",
                                4: "Symbolic Logic and Its Applications",
                                5: "Truth, Validity, and Soundness in Argumentation",
                            },
                        },
                        2: {
                            "title": "The Scope of Logic",
                            "sections": {
                                1: "Consequence and Validity",
                                2: "Cases and Types of Validity",
                                3: "Formal Validity",
                                4: "Sound Arguments",
                                5: "Inductive Arguments",
                            },
                        },
                        3: {
                            "title": "Other Logical Notions",
                            "sections": {},
                        },
                    },
                },
                "II": {
                    "title": "Truth-functional Logic",
                    "chapters": {
                        1: {
                            "title": "Logical Operators",
                            "sections": {
                                1: "Negation",
                                2: "Conjunction",
                                3: "Disjunction",
                                4: "Conditional Statements",
                                5: "Biconditional Statements",
                            },
                        },
                        2: {
                            "title": "Truth Tables for Operators",
                            "sections": {
                                1: "Constructing Truth Tables",
                                2: "Using Truth Tables for Validation",
                                3: "Determining Logical Equivalences",
                                4: "Common Logical Identities",
                            },
                        },
                    },
                },
                "III": {
                    "title": "Truth-tables",
                    "chapters": {
                        1: {
                            "title": "Basics of Truth-tables",
                            "sections": {
                                1: "Truth-table Setup",
                                2: "Analyzing Statements",
                                3: "Validating Arguments",
                            },
                        },
                        2: {
                            "title": "Applications of Truth-tables",
                            "sections": {
                                1: "Solving Logical Puzzles",
                                2: "Modeling Logical Circuits",
                                3: "Advanced Truth-table Techniques",
                            },
                        },
                    },
                },
            },
        },
    ],
}

