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
        "description": "This card explores the foundational ",
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
            "slug": "forallx",
            "title": "$ \\forall x $",
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
                                5: "Truth, Validity, and Soundness in Argumentation"
                            }
                        },
                        2: {
                            "title": "The Scope of Logic",
                            "sections": {
                                1: "Consequence and Validity",
                                2: "Cases and Types of Validity",
                                3: "Formal Validity",
                                4: "Sound Arguments",
                                5: "Inductive Arguments"
                            }
                        },
                        3: {
                            "title": "Other Logical Notions",
                            "sections": {}
                        }
                    }
                },
                "II": {
                    "title": "Truth-functional Logic",
                    "chapters": {
                        4: {
                            "title": "Logical Operators",
                            "sections": {
                                1: "Negation",
                                2: "Conjunction",
                                3: "Disjunction",
                                4: "Conditional Statements",
                                5: "Biconditional Statements"
                            }
                        },
                        5: {
                            "title": "Truth Tables for Operators",
                            "sections": {
                                1: "Constructing Truth Tables",
                                2: "Using Truth Tables for Validation",
                                3: "Determining Logical Equivalences",
                                4: "Common Logical Identities"
                            }
                        }
                    }
                },
                "III": {
                    "title": "Truth-tables",
                    "chapters": {
                        6: {
                            "title": "Basics of Truth-tables",
                            "sections": {
                                1: "Truth-table Setup",
                                2: "Analyzing Statements",
                                3: "Validating Arguments"
                            }
                        },
                        7: {
                            "title": "Applications of Truth-tables",
                            "sections": {
                                1: "Solving Logical Puzzles",
                                2: "Modeling Logical Circuits",
                                3: "Advanced Truth-table Techniques"
                            }
                        }
                    }
                }
            }
        },
        {
            "slug": "logic_basics",
            "title": "Logic Basics",
            "parts": {
                "I": {
                    "title": "Introduction to Logic",
                    "chapters": {
                        1: {
                            "title": "Understanding Arguments",
                            "sections": {
                                1: "What is an Argument?",
                                2: "Structure of Arguments",
                                3: "Premises and Conclusions",
                                4: "Soundness and Validity",
                                5: "Common Logical Forms",
                                6: "Counterexamples"
                            }
                        },
                        2: {
                            "title": "Propositional Logic",
                            "sections": {
                                1: "Propositions Defined",
                                2: "Negation and Disjunction",
                                3: "Truth Tables",
                                4: "Conditional Statements",
                                5: "Biconditional Statements",
                                6: "Logical Equivalences"
                            }
                        },
                        3: {
                            "title": "Quantifiers and Variables",
                            "sections": {
                                1: "Introduction to Quantifiers",
                                2: "Universal Quantifiers",
                                3: "Existential Quantifiers",
                                4: "Scope and Binding",
                                5: "Quantifier Equivalences",
                                6: "Nested Quantifiers"
                            }
                        }
                    }
                },
                "II": {
                    "title": "Intermediate Logic Topics",
                    "chapters": {
                        4: {
                            "title": "Logical Fallacies",
                            "sections": {
                                1: "Formal Fallacies",
                                2: "Informal Fallacies",
                                3: "Fallacies of Ambiguity",
                                4: "False Dichotomy",
                                5: "Circular Reasoning",
                                6: "Appeal to Emotion"
                            }
                        },
                        5: {
                            "title": "Proofs and Arguments",
                            "sections": {
                                1: "Direct Proofs",
                                2: "Indirect Proofs",
                                3: "Proof by Contradiction",
                                4: "Mathematical Induction",
                                5: "Proof Strategies",
                                6: "Analyzing Proof Errors"
                            }
                        }
                    }
                }
            }
        },
        {
            "slug": "advanced_logic_principles",
            "title": "Advanced Logic Principles",
            "parts": {
                "I": {
                    "title": "Logic Foundations",
                    "chapters": {
                        1: {
                            "title": "Philosophy of Logic",
                            "sections": {
                                1: "What is Logic?",
                                2: "Historical Context",
                                3: "Types of Logic",
                                4: "Theoretical Approaches",
                                5: "Practical Applications",
                                6: "Ethics in Logical Reasoning"
                            }
                        },
                        2: {
                            "title": "Logical Syntax",
                            "sections": {
                                1: "Grammar of Logic",
                                2: "Syntax Rules",
                                3: "Symbol Systems",
                                4: "Logical Consistency",
                                5: "Parsing Logical Sentences",
                                6: "Advanced Syntax Analysis"
                            }
                        },
                        3: {
                            "title": "Logical Semantics",
                            "sections": {
                                1: "Understanding Semantics",
                                2: "Denotation vs Connotation",
                                3: "Semantic Truth",
                                4: "Logical Implications",
                                5: "Formal vs Informal Semantics",
                                6: "Applications of Semantics"
                            }
                        }
                    }
                },
                "II": {
                    "title": "Symbolic Logic",
                    "chapters": {
                        4: {
                            "title": "Propositional Logic",
                            "sections": {
                                1: "Basics of Propositions",
                                2: "Logical Connectives",
                                3: "Propositional Logic Systems",
                                4: "Truth Tables and Models",
                                5: "Formal Logical Deduction",
                                6: "Applications in Computation"
                            }
                        },
                        5: {
                            "title": "Predicate Logic",
                            "sections": {
                                1: "Introduction to Predicates",
                                2: "Quantifiers",
                                3: "Variables and Predicates",
                                4: "Logical Formulas",
                                5: "Advanced Predicate Analysis",
                                6: "Computation with Predicates"
                            }
                        }
                    }
                }
            }
        },
                {
            "slug": "advanced_logic_principles",
            "title": "Advanced Logic Principles",
            "parts": {
                "I": {
                    "title": "Logic Foundations",
                    "chapters": {
                        1: {
                            "title": "Philosophy of Logic",
                            "sections": {
                                1: "What is Logic?",
                                2: "Historical Context",
                                3: "Types of Logic",
                                4: "Theoretical Approaches",
                                5: "Practical Applications",
                                6: "Ethics in Logical Reasoning"
                            }
                        },
                        2: {
                            "title": "Logical Syntax",
                            "sections": {
                                1: "Grammar of Logic",
                                2: "Syntax Rules",
                                3: "Symbol Systems",
                                4: "Logical Consistency",
                                5: "Parsing Logical Sentences",
                                6: "Advanced Syntax Analysis"
                            }
                        },
                        3: {
                            "title": "Logical Semantics",
                            "sections": {
                                1: "Understanding Semantics",
                                2: "Denotation vs Connotation",
                                3: "Semantic Truth",
                                4: "Logical Implications",
                                5: "Formal vs Informal Semantics",
                                6: "Applications of Semantics"
                            }
                        }
                    }
                },
                "II": {
                    "title": "Symbolic Logic",
                    "chapters": {
                        4: {
                            "title": "Propositional Logic",
                            "sections": {
                                1: "Basics of Propositions",
                                2: "Logical Connectives",
                                3: "Propositional Logic Systems",
                                4: "Truth Tables and Models",
                                5: "Formal Logical Deduction",
                                6: "Applications in Computation"
                            }
                        },
                        5: {
                            "title": "Predicate Logic",
                            "sections": {
                                1: "Introduction to Predicates",
                                2: "Quantifiers",
                                3: "Variables and Predicates",
                                4: "Logical Formulas",
                                5: "Advanced Predicate Analysis",
                                6: "Computation with Predicates"
                            }
                        }
                    }
                }
            }
        },
                {
            "slug": "advanced_logic_principles",
            "title": "Advanced Logic Principles",
            "parts": {
                "I": {
                    "title": "Logic Foundations",
                    "chapters": {
                        1: {
                            "title": "Philosophy of Logic",
                            "sections": {
                                1: "What is Logic?",
                                2: "Historical Context",
                                3: "Types of Logic",
                                4: "Theoretical Approaches",
                                5: "Practical Applications",
                                6: "Ethics in Logical Reasoning"
                            }
                        },
                        2: {
                            "title": "Logical Syntax",
                            "sections": {
                                1: "Grammar of Logic",
                                2: "Syntax Rules",
                                3: "Symbol Systems",
                                4: "Logical Consistency",
                                5: "Parsing Logical Sentences",
                                6: "Advanced Syntax Analysis"
                            }
                        },
                        3: {
                            "title": "Logical Semantics",
                            "sections": {
                                1: "Understanding Semantics",
                                2: "Denotation vs Connotation",
                                3: "Semantic Truth",
                                4: "Logical Implications",
                                5: "Formal vs Informal Semantics",
                                6: "Applications of Semantics"
                            }
                        }
                    }
                },
                "II": {
                    "title": "Symbolic Logic",
                    "chapters": {
                        4: {
                            "title": "Propositional Logic",
                            "sections": {
                                1: "Basics of Propositions",
                                2: "Logical Connectives",
                                3: "Propositional Logic Systems",
                                4: "Truth Tables and Models",
                                5: "Formal Logical Deduction",
                                6: "Applications in Computation"
                            }
                        },
                        5: {
                            "title": "Predicate Logic",
                            "sections": {
                                1: "Introduction to Predicates",
                                2: "Quantifiers",
                                3: "Variables and Predicates",
                                4: "Logical Formulas",
                                5: "Advanced Predicate Analysis",
                                6: "Computation with Predicates"
                            }
                        }
                    }
                }
            }
        }
    ]
}

