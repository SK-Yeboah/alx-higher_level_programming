#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list) {
    listint_t *slow = list;  /* Slow pointer */
    listint_t *fast = list;  /* Fast pointer */

    /* Traverse the list with slow and fast pointers */
    while (slow != NULL && fast != NULL && fast->next != NULL) {
        slow = slow->next;        /* Move slow pointer by one step */
        fast = fast->next->next;  /* Move fast pointer by two steps */

        /* If there is a cycle, slow and fast pointers will meet */
        if (slow == fast) {
            return (1);  /* Cycle detected */
        }
    }

    return (0);  /* No cycle found */
}
