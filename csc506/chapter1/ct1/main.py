"""
CSC506 — Critical Thinking 1
Data Structure Learning & Complexity Analysis Tool

Implements stack, queue, and linked list from scratch using nodes.
Demonstrates operations, predicts Big-O complexity, and compares
predicted vs actual performance with charts.
"""

import time
import os

# Node — the basic building block that holds a value and points to the next node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Stack — Last-In, First-Out. Think of a stack of plates: you always
# take from the top and put new ones on top.
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        #Add a value to the top of the stack.
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        # Remove and return the top value. Returns None if empty.
        if not self.top:
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        # Look at the top value without removing it
        return self.top.value if self.top else None

    def to_list(self):
        # Return all values as a list from top to bottom (for display)
        result, curr = [], self.top
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


# Queue — First-In, First-Out. Like a line at a store: the first person
# in line is the first one served.
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        # Add a value to the back of the queue
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        # Remove and return the front value. Returns None if empty
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return value

    def to_list(self):
        # Return all values as a list from front to back (for display)
        result, curr = [], self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


# Linked List — a chain of nodes where each one points to the next.
# Good for when you need to insert or remove items frequently without
# shifting everything around like you would with an array.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_front(self, value):
        # Add a new node at the very beginning of the list
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insert_end(self, value):
        # Add a new node at the very end of the list
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def delete(self, value):
        """ Walk through the list, find the value, and remove that node.
        Returns True if found and deleted, False if not found """
        curr, prev = self.head, None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                if curr == self.tail:
                    self.tail = prev
                self.size -= 1
                return True
            prev, curr = curr, curr.next
        return False

    def search(self, value):
        # Walk through the list looking for a value. Returns True if found, False otherwise
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def to_list(self):
        # Return all values as a list from head to tail (for display)
        result, curr = [], self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


# Helpers that build up a data structure with n items so we can test performance
def build_stack(n):
    # Create a stack with values 0 through n-1
    s = Stack()
    for i in range(n):
        s.push(i)
    return s

def build_queue(n):
    # Create a queue with values 0 through n-1
    q = Queue()
    for i in range(n):
        q.enqueue(i)
    return q

def build_linked_list(n):
    # Create a linked list with values 0 through n-1
    ll = LinkedList()
    for i in range(n):
        ll.insert_end(i)
    return ll


# Demos — show each data structure in action with simple examples
def demo_stack():
    # Show how a stack works — push items on, pop them off in reverse order
    print("=" * 50)
    print("STACK DEMO (LIFO)")
    print("Use case: undo/redo, bracket matching, recursion")
    print("=" * 50)

    s = Stack()
    for v in [10, 20, 30]:
        s.push(v)
        print(f"  push({v})  → {s.to_list()}")

    print(f"  peek()   → {s.peek()}")
    print(f"  pop()    → {s.pop()},  stack: {s.to_list()}")
    print(f"  pop()    → {s.pop()},  stack: {s.to_list()}")
    print()


def demo_queue():
    # Show how a queue works — first item in is the first item out
    print("=" * 50)
    print("QUEUE DEMO (FIFO)")
    print("Use case: task scheduling, BFS, print queue")
    print("=" * 50)

    q = Queue()
    for v in ["task_A", "task_B", "task_C"]:
        q.enqueue(v)
        print(f"  enqueue('{v}')  → {q.to_list()}")

    print(f"  dequeue() → '{q.dequeue()}',  queue: {q.to_list()}")
    print(f"  dequeue() → '{q.dequeue()}',  queue: {q.to_list()}")
    print()


def demo_linked_list():
    # Show how a linked list works — insert, delete, and search through nodes
    print("=" * 50)
    print("LINKED LIST DEMO")
    print("Use case: dynamic insert/delete, playlists")
    print("=" * 50)

    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.insert_end(v)
    print(f"  insert_end(1,2,3)    → {ll.to_list()}")

    ll.insert_front(0)
    print(f"  insert_front(0)      → {ll.to_list()}")

    ll.delete(2)
    print(f"  delete(2)            → {ll.to_list()}")

    print(f"  search(3)            → {ll.search(3)}")
    print(f"  search(99)           → {ll.search(99)}")
    print()


# Complexity Prediction Table — what we expect each operation's Big-O to be
def print_complexity_table():
    """Print a table showing the predicted time and space complexity
    for every operation across all three data structures"""
    print("=" * 60)
    print("COMPLEXITY PREDICTIONS (Time / Space per operation)")
    print("=" * 60)
    print(f"  {'Operation':<28} {'Time':<10} {'Space':<10}")
    print("  " + "-" * 48)

    rows = [
        ("Stack.push",              "O(1)", "O(1)"),
        ("Stack.pop",               "O(1)", "O(1)"),
        ("Stack.search",            "O(n)", "O(1)"),
        ("Queue.enqueue",           "O(1)", "O(1)"),
        ("Queue.dequeue",           "O(1)", "O(1)"),
        ("Queue.search",            "O(n)", "O(1)"),
        ("LinkedList.insert_front", "O(1)", "O(1)"),
        ("LinkedList.insert_end",   "O(1)", "O(1)"),
        ("LinkedList.delete",       "O(n)", "O(1)"),
        ("LinkedList.search",       "O(n)", "O(1)"),
    ]
    for name, t, s in rows:
        print(f"  {name:<28} {t:<10} {s:<10}")

    print(f"\n  Overall structure space: O(n)")
    print()


# Performance Testing
def measure(operation, generator, sizes, trials=5):
    """Run an operation at different input sizes and record how long it takes.
    Repeats each size 5 times and takes the median to reduce noise"""
    import statistics
    results = []
    for n in sizes:
        times = []
        for _ in range(trials):
            ds = generator(n)
            start = time.perf_counter()
            operation(ds)
            times.append(time.perf_counter() - start)
        results.append((n, statistics.median(times)))
    return results


def classify(results):
    # Look at how the times change as input grows and decide if it's constant O(1) or linear O(n)
    ns = [n for n, _ in results]
    ts = [t for _, t in results]
    if max(ts) - min(ts) < 1e-6:
        return "O(1)"
    # check if time grows proportionally to n
    ratio_start = ts[0] / ns[0] if ns[0] else 0
    ratio_end = ts[-1] / ns[-1] if ns[-1] else 0
    if ratio_end > 0 and 0.3 < ratio_start / ratio_end < 3.0:
        return "O(n)"
    return "O(1)"


def run_performance_tests():
    """Actually time each operation and compare the measured complexity
    against what we predicted. Prints a table showing if they match"""
    print("=" * 60)
    print("PERFORMANCE TESTING — Predicted vs Actual")
    print("=" * 60)

    sizes = [500, 1000, 2000, 4000, 8000]

    tests = [
        ("Stack.push",       lambda ds: ds.push(0),          build_stack,       "O(1)"),
        ("Stack.pop",        lambda ds: ds.pop(),             build_stack,       "O(1)"),
        ("Queue.enqueue",    lambda ds: ds.enqueue(0),        build_queue,       "O(1)"),
        ("Queue.dequeue",    lambda ds: ds.dequeue(),         build_queue,       "O(1)"),
        ("LL.insert_front",  lambda ds: ds.insert_front(0),   build_linked_list, "O(1)"),
        ("LL.insert_end",    lambda ds: ds.insert_end(0),     build_linked_list, "O(1)"),
        ("LL.search(worst)", lambda ds: ds.search(-1),        build_linked_list, "O(n)"),
        ("LL.delete(last)",  lambda ds: ds.delete(ds.size - 1), build_linked_list, "O(n)"),
    ]

    all_results = []
    print(f"\n  {'Operation':<20} {'Predicted':<12} {'Measured':<12} {'Match'}")
    print("  " + "-" * 54)

    for name, op, gen, predicted in tests:
        results = measure(op, gen, sizes)
        measured = classify(results)
        match = "YES" if predicted == measured else "NO"
        print(f"  {name:<20} {predicted:<12} {measured:<12} {match}")
        all_results.append((name, predicted, results))

    print()
    return all_results


# Chart Generation
def generate_charts(all_results):
    """Create two charts: one showing how runtime grows with input size,
    and another comparing our predictions against what actually happened."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not installed — skipping charts.")
        print("  Install with: pip install matplotlib")
        return

    output_dir = os.path.dirname(os.path.abspath(__file__))

    # Chart 1: Runtime vs input size
    fig, ax = plt.subplots(figsize=(10, 6))
    for name, _, results in all_results:
        ns = [n for n, _ in results]
        ts = [t for _, t in results]
        ax.plot(ns, ts, marker="o", label=name)
    ax.set_xlabel("Input Size (n)")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Runtime vs Input Size")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    path1 = os.path.join(output_dir, "chart_runtime.png")
    fig.savefig(path1, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path1}")

    # Chart 2: Predicted vs actual comparison
    names = [name for name, _, _ in all_results]
    predicted = [p for _, p, _ in all_results]
    measured = [classify(r) for _, _, r in all_results]
    colors = ["#2ecc71" if p == m else "#e74c3c" for p, m in zip(predicted, measured)]

    fig, ax = plt.subplots(figsize=(10, 5))
    y = range(len(names))
    avg_times = [sum(t for _, t in r) / len(r) for _, _, r in all_results]
    ax.barh(list(y), avg_times, color=colors, edgecolor="black", alpha=0.8)
    ax.set_yticks(list(y))
    ax.set_yticklabels([f"{n}  [pred:{p} actual:{m}]"
                        for n, p, m in zip(names, predicted, measured)])
    ax.set_xlabel("Mean Time (seconds)")
    ax.set_title("Predicted vs Actual Complexity (green=match, red=mismatch)")
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    path2 = os.path.join(output_dir, "chart_comparison.png")
    fig.savefig(path2, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path2}")


# Main entry point — run demos, print complexity table, run performance tests, and generate charts
if __name__ == "__main__":
    demo_stack()
    demo_queue()
    demo_linked_list()
    print_complexity_table()
    results = run_performance_tests()
    generate_charts(results)
