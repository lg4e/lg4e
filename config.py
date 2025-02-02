# Markdown 渲染所需扩展
from markdown.extensions import fenced_code,  sane_lists, tables,  attr_list, smarty, codehilite, nl2br, extra

MARKDOWN_EXTENSIONS = [
    fenced_code.FencedCodeExtension(),
    tables.TableExtension(),
    attr_list.AttrListExtension(),  #  支持自定义属性，例如 {#id .class key=value}
    codehilite.CodeHiliteExtension(
        linenums=False,  # 显示行号
        guess_lang=False,  # 禁止语言自动猜测
        pygments_style="default"  # 使用默认代码高亮样式
    ),
    smarty.SmartyExtension(),  #  支持智能标点（连字符、引号等优化）
    sane_lists.SaneListExtension(),
    nl2br.Nl2BrExtension(),  #  将换行符保留为 HTML 的 <br> 标签
    extra.ExtraExtension()  #  完整 Markdown 支持（列表、引用、加粗等）
]

# 默认模板文件
DEFAULT_404_TEMPLATE = "404.html"
DEFAULT_500_TEMPLATE = "500.html"

# 分类数据
CATEGORIES = {
    "history_of_logic": {
        "title": "A Study Guide",
        "description": "A Study Guide・・・",
    },
    "introduction_to_logic": {
        "title": "Introduction to Logic",
        "description": "In a republican nation, whose citizens are to be led by persuasion and not by force, the art of reasoning becomes of the first importance.",
    },
    "set_theory_and_logic": {
        "title": "Set Theory and Logic",
        "description": "An introduction to Set Theory and Logic",
    },
    "formal_logic": {
        "title": "Formal Logic",
        "description": "An Introduction to Formal Logic",
    },
    "Ⅲ": {
        "title": "Ⅲ ",
        "description": "This card ・・・",
    },
    "Ⅳ": {
        "title": "Ⅳ",
        "description": "This card ・・・",
    },
    "Ⅴ": {
        "title": "Ⅴ",
        "description": "This card ・・・",
    },
    "Ⅵ": {
        "title": "Ⅵ",
        "description": "This card ・・・",
    },
    "Ⅶ": {
        "title": "Ⅶ",
        "description": "This card ・・・",
    },
    "Ⅷ": {
        "title": "Ⅷ",
        "description": "This card ・・・",
    },
    "Ⅸ": {
        "title": "Ⅸ",
        "description": "This card ・・・",
    },
    "Ⅹ": {
        "title": "Ⅹ",
        "description": "This card ・・・",
    },
}

# 书籍数据
BOOKS = {
    "introduction_to_logic": [
        {
            "slug": "introduction_to_logic",
            "title": "逻辑学导论",
            "parts": {
                "I": {
                    "title": "Logic and Language",
                    "chapters": {
                        1: {
                            "title": "逻辑学的基本概念 // Basic Logical Concepts",
                            "sections": {
                                1: "什么是逻辑学 // What Logic Is",
                                2: "命题与论证 // Propositions and Arguments",
                                3: "论证的辨识 // Recognizing Arguments",
                                4: "论证与说明 // Arguments and Explanations",
                                5: "演绎论证与归纳论证 // Dedactive and Inductive Arguments",
                                6: "有效性与真实性 // Validity and Truth",
                            }
                        },
                        2: {
                            "title": "论证的分析 // Analyzing Arguments",
                            "sections": {
                                1: "论证的重塑 // Paraphrasing Argument",
                                2: "论证的图示 // Diagramming Arguments",
                                3: "复杂的论证性语段 // Complex Argumentatative Passages",
                                4: "推理中的问题 // Problems in Reasoning",
                            }
                        },
                        3: {
                            "title": "语言与定义 // Language and Definitions",
                            "sections": {
                                1: "语言的功能 // Language Functions",
                                2: "情感语言、中性语言与论争 // Emotive Language, Neutral Language, and Disputes",
                                3: "论争与含混性 // Disputes and Ambiguity",
                                4: "定义及其用途 // Definitions and Their Uses",
                                5: "定义的结构：外延与内涵 // The Structure of Definitions: Extension and Intension",
                                6: "属加种差定义 // Definition by Genus and Difference",
                            }
                        },
                        4: {
                            "title": "谬误 // Fallacies",
                            "sections": {
                                1: "什么是谬误 // What Is a Fallacies",
                                2: "谬误的分类 // Classification of Fallacies",
                                3: "相干谬误 // Fallacies of Relevance",
                                4: "不当归纳谬误 // Fallacies of Defective Induction",
                                5: "预设谬误 // Fallacies of Presumption",
                                6: "含混谬误 // Fallacies of Ambiguity",
                            }
                        }
                    }
                },
               "II": {
                    "title": "Deduction",
                    "chapters": {
                        5: {
                            "title": "直言命题 // Categorical Propositions",
                            "sections": {
                                1: "演绎理论 // The Theory of Deduction",
                                2: "类与直言命题 // Classes and Categorical Propositions",
                                3: "四种直言命题 // The Four Kinds of Categorical Propositions",
                                4: "质、量与周延性 // Quality, Quantity, and Distribution",
                                5: "传统对当方阵 // The Traditional Square of Opposition",
                                6: "其他直接推论 // Further Immediate Inferences",
                                7: "存在含义与直言命题的解释 // Existential Import and the Interpretation of Categorical Propositions",
                                8: "直言命题的符号系统与图解 // Symbolism and Diagrams for Categorical Propositions",
                            }
                        },
                        6: {
                            "title": "直言三段论 // Categorical Syllogisms",
                            "sections": {
                                1: "直言三段论的标准形式 // Standard-Form Categorical Syllogisms",
                                2: "三段论论证的形式性质 // The Formal Nature of Syllogistic Argument",
                                3: "检验三段论：文恩图解法 // Venn Diagram Technique for Testing Syllogisms",
                                4: "三段论规则与三段论谬误 // Syllogistic Rules and Syllogistic Fallacies",
                                5: "直言三段论的15个有效形式 // Exposition of the Fifteen Valid Forms of the Categorical Syllogism",
                            }
                        },
                        7: {
                            "title": "日常语言中的论证 // Syllogisms in Ordinary Language",
                            "sections": {
                                1: "三段论论证 // Syllogistic Arguments",
                                2: "词项数量归约为三 // Reducing the Number of Terms to Three",
                                3: "直言命题的标准化 // Translating Categorical Propositions into Standard Form",
                                4: "协同翻译 // Uniform Translation",
                                5: "省略式三段论 // Enthymemes",
                                6: "连锁三段论 // Sorites",
                                7: "析取三段论与假言三段论 // Disjunctive and Hypothetical Syllogisms",
                                8: "二难推论 // The Dilemma",
                            }
                        },
                        8: {
                            "title": "命题逻辑Ⅰ：真值函项陈述与论证 // Truth-Functional Statements and Arguments",
                            "sections": {
                                1: "现代逻辑及其符号语言 // Modern Logic and Its Symbolic Language",
                                2: "真值函项性：简单陈述与复合陈述 // Truth-Functionality: Simple Statements and Compound Statements",
                                3: "合取、否定与析取 // Conjunction, Negation, and Disjunction",
                                4: "条件陈述与实质蕴涵 // Conditional Statements and Material Implication",
                                5: "论证形式与运用逻辑类推进行的反驳 // Argument Forms and Refutation by Logical Analogy",
                                6: "“无效”和“有效”的精确含义 // The Precise Meaning of “Valid” and “Invalid”",
                                7: "根据真值表验证论证：完备的真值表方法 // Testing Argument Validity Using Truth Tables: The Complete Truth-Table Method (CTTM)",
                                8: "一些常见的论证形式 // Some Common Argument Forms",
                                9: "陈述形式与实质等值 // Statement Forms and Material Equivalence A. Statement Forms and Statements",
                                10: "逻辑等价 // Logical Equivalence",
                                11: "三大“思想法则”：逻辑的原理 // The Three “Laws of Thought”: Principles of Logic",
                            }
                        },
                        9: {
                            "title": "命题逻辑Ⅱ：演绎方法 // Propositional Logic II Methods of Deduction",
                            "sections": {
                                1: "有效性的形式证明 // Formal Proof of Validity",
                                2: "基本的有效论证形式 // The Elementary Valid Argument Forms",
                                3: "有效性形式证明示例 // Formal Proofs of Validity Exhibited",
                                4: "有效性形式证明的构造 // Constructing Formal Proofs of Validity",
                                5: "构造更复杂的形式证明 // Constructing More Extended Formal Proofs",
                                6: "扩展推论规则：替换规则 // Expanding the Rules of Inference: Replacement Rules",
                                7: "自然演绎系统 // The System of Natural Deduction",
                                8: "运用19个推论规则构建形式证明 // Constructing Formal Proofs Using the Nineteen Rules of Inference",
                                9: "简化的真值表方法 // Shorter Truth-Table Technique (STTT)",
                                10: "不相容性 // Inconsistency",
                                11: "条件证明 // Conditional Proof",
                                12: "间接证明 // Indirect Proof",
                                13: "可靠性论证与笃证性论证的辨别 // Sound Arguments and Demonstrative Arguments Distinguished",
                            }
                        },
                        10: {
                            "title": "谓词逻辑：量化理论 // Predicate Logic: Quantifi cation Theory",
                            "sections": {
                                1: "量化的必要性 // The Need for Quantification",
                                2: "单称命题 // Singular Propositions",
                                3: "全称量词与存在量词 // Universal and Existential Quantifiers",
                                4: "传统主谓命题 // Traditional Subject–Predicate Propositions",
                                5: "有效性证明 // Proving Validity",
                                6: "无效性证明 // Proving Invalidity",
                                7: "非三段论推论 // Asyllogistic Inference",
                            }
                        }

                    }
                },
              "III": {
                    "title": "Induction",
                    "chapters": {
                        11: {
                            "title": "类比推理 // Analogical Reasoning",
                            "sections": {
                                1: "归纳与演绎再探 // Induction and Deduction Revisited",
                                2: "类比论证 // Argument by Analogy",
                                3: "类比论证的评价 // Appraising Analogical Arguments",
                                4: "通过逻辑类推进行的反驳 // Refutation by Logical Analogy",
                            }
                        },
                        12: {
                            "title": "因果推理 // Causal Reasoning",
                            "sections": {
                                1: "原因与结果 // Cause and Effect",
                                2: "因果律与自然齐一性 // Causal Laws and the Uniformity of Nature",
                                3: "简单枚举归纳法 // Induction by Simple Enumeration",
                                4: "因果分析的方法 // Methods of Causal Analysis",
                                5: "归纳技术的局限 // Limitations of Inductive Techniques",
                            }
                        },
                        13: {
                            "title": "科学与假说 // Science and Hypothesis",
                            "sections": {
                                1: "科学说明 // Scientific Explanation",
                                2: "科学探究：假说与证实 // Scientific Inquiry: Hypothesis and Confirmation",
                                3: "对竞争性科学说明的评价 // Evaluating Competing Scientifi c Explanations",
                                4: "作为假说的分类 // Classifi cation as Hypothesis",
                            }
                        },
                        14: {
                            "title": "概率 //  Probability",
                            "sections": {
                                1: "关于概率的几种观点 // Alternative Conceptions of Probability",
                                2: "概率演算 // The Probability Calculus",
                                3: "日常生活中的概率 // Probability in Everyday Life",
                            }
                        }
                    }
                }
            }
        },
        {
            "slug": "port_royal_logic",
            "title": "Logic, or The art of thinking: being the Port-Royal logic",
            "parts": {
                "I": {
                    "title": "Logic and Language",
                    "chapters": {
                        1: {
                            "title": "Basic Logical Concepts // 逻辑学的基本概念",
                            "sections": {
                                1: "What Logic Is // 什么是逻辑学",
                                2: "Propositions and Arguments // 命题与论证",
                                3: "Recognizing Arguments // 论证的辨识",
                                4: "Arguments and Explanations",
                                5: "Dedactive and Inductive Arguments",
                                6: "Validity and Truth",
                            },
                        },
                        2: {
                            "title": "论证的分析 // Analyzing Arguments",
                            "sections": {
                                1: "Paraphrasing Argument",
                                2: "Propositions and Arguments",
                                3: "Recognizing Arguments",
                                4: "Arguments and Explanations",
                                5: "Dedactive and Inductive Arguments",
                                6: "Validity and Truth",
                            },
                        },

                    },
                },
            },
        },

    ],        
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
            "title": "$ \\forall x $ : An Introduction to Formal Logic",
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

