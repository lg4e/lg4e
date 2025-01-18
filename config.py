# Markdown 渲染所需扩展
from markdown.extensions import fenced_code, tables

MARKDOWN_EXTENSIONS = [
    fenced_code.FencedCodeExtension(),
    tables.TableExtension()
]

# 默认模板文件
DEFAULT_404_TEMPLATE = "404.html"
DEFAULT_500_TEMPLATE = "500.html"

CARDS = {
    # Set Theory and Logic Card
    "set_theory_and_logic": {
        "title": "Set Theory and Logic",
        "description": "This card is an introduction to Set Theory, aimed especially at ...",
        "chapters": {
            1: {"title": "Fundamental Concepts"},
            2: {"title": "Functions"},
            3: {"title": "Relations"},
            4: {"title": "The Integers and the Real Numbers"},
            5: {"title": "Cartesian Products"},
            6: {"title": "Finite Sets"},
            7: {"title": "Countable and Uncountable Sets"},
            8: {"title": "The Principle of Recursive Definition"},
            9: {"title": "Infinite Sets and the Axiom of Choice"},
            10: {"title": "Well-Ordered Sets"},
        },
    },

    # Formal Logic Card
    "formal_logic": {
        "title": "Formal Logic",
        "description": "An Introduction to Formal Logic",
        "chapters": {
            1: {
                "title": "Key notions of logic",
                "subchapters": {
                    1: "Arguments",
                    2: "The scope of logic",
                    3: "Other logical notions",
                },
            },
            2: {
                "title": "Truth-functional logic",
                "subchapters": {
                    1: "First steps to symbolization",
                    2: "Connectives",
                    3: "Sentences of TFL",
                    4: "Ambiguity",
                    5: "Use and mention",
                },
            },
            3: {
                "title": "Truth tables",
                "subchapters": {
                    1: "Characteristic truth tables",
                    2: "Truth-functional connectives",
                    3: "Complete truth tables",
                },
            },
        },
    },

    # Linear Algebra Card
    "linear_algebra": {
        "title": "Linear Algebra",
        "description": "This card explores the foundational concepts of linear algebra.",
        "chapters": {
            1: {"title": "Vectors and Matrices"},
            2: {"title": "Determinants"},
            3: {"title": "Eigenvalues and Eigenvectors"},
            4: {"title": "Vector Spaces"},
            5: {"title": "Linear Transformations"},
        },
    },

    # Calculus Card
    "calculus": {
        "title": "Calculus",
        "description": "This card focuses on the essential topics in calculus.",
        "chapters": {
            1: {"title": "Limits and Continuity"},
            2: {"title": "Differentiation"},
            3: {"title": "Integration"},
            4: {"title": "Applications of Derivatives"},
            5: {"title": "Series and Sequences"},
        },
    },

    # Discrete Mathematics Card
    "discrete_math": {
        "title": "Discrete Mathematics",
        "description": "This card covers fundamental topics in discrete math.",
        "chapters": {
            1: {"title": "Propositional Logic"},
            2: {"title": "Combinatorics"},
            3: {"title": "Graph Theory"},
            4: {"title": "Recursion and Recurrence Relations"},
            5: {"title": "Boolean Algebra"},
        },
    },

    # Abstract Algebra Card
    "abstract_algebra": {
        "title": "Abstract Algebra",
        "description": "This card delves into groups, rings, and fields.",
        "chapters": {
            1: {"title": "Groups"},
            2: {"title": "Rings"},
            3: {"title": "Fields"},
            4: {"title": "Modules and Vector Spaces"},
            5: {"title": "Homomorphisms"},
        },
    },

    # Probability Theory Card
    "probability_theory": {
        "title": "Probability Theory",
        "description": "This card introduces key concepts in probability.",
        "chapters": {
            1: {"title": "Random Variables"},
            2: {"title": "Probability Distributions"},
            3: {"title": "Expected Value and Variance"},
            4: {"title": "Conditional Probability"},
            5: {"title": "The Law of Large Numbers"},
        },
    },

    # Real Analysis Card
    "real_analysis": {
        "title": "Real Analysis",
        "description": "This card explores rigorous calculus topics.",
        "chapters": {
            1: {"title": "Real Numbers and Sequences"},
            2: {"title": "Limits and Continuity"},
            3: {"title": "Differentiation"},
            4: {"title": "Integration"},
            5: {"title": "Metric Spaces"},
        },
    },

    # Computer Science Basics Card
    "computer_science_basics": {
        "title": "Computer Science Basics",
        "description": "This card introduces fundamental concepts in computer science.",
        "chapters": {
            1: {"title": "Algorithms"},
            2: {"title": "Data Structures"},
            3: {"title": "Complexity Theory"},
            4: {"title": "Operating Systems"},
            5: {"title": "Networks"},
        },
    },

    # Graph Theory Card
    "graph_theory": {
        "title": "Graph Theory",
        "description": "This card dives into the structure and properties of graphs.",
        "chapters": {
            1: {"title": "Graphs and Subgraphs"},
            2: {"title": "Paths and Cycles"},
            3: {"title": "Connectivity"},
            4: {"title": "Graph Coloring"},
            5: {"title": "Planar Graphs"},
        },
    },
}

