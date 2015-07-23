#!/usr/bin/python

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() +'>')

def helper(link):
    if isinstance(link.first, Link):
        first = '<' + helper(link.first).rstrip() + '>'
    else:
        first = str(link.first)

    if link.rest != Link.empty:
        return first + ' ' + helper(link.rest)
    else:
        return first + ' '
    

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    if len(lst) == 1:
        return Link(lst[0])
    return Link(lst[0], list_to_link(lst[1:]))


def main():
    link = list_to_link([1, 2, 3])
    print_link(link)

    link = Link(1, Link(2, Link(3)))
    print_link(link)
    link1 = Link(1, Link(Link(2), Link(3)))
    print_link(link1)
    link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    print_link(link1)


if __name__ == '__main__':
    main()
